import logging

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models import get_model
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.contrib.auth import authenticate, login

import twitter
import signals

logger = logging.getLogger(__name__)

@require_GET
def twitter_oauth_begin(request):
    signals.twitter_auth_started.send(sender="ecl_twitter")

    client = twitter.Twitter()
    data = client.generate_authorization_url()
    token = data['oauth_token']
    secret = data['oauth_token_secret']

    request.session['temporary_oauth_token'] = token
    request.session['temporary_oauth_secret'] = secret
    url = twitter.TWITTER_BASE_URL + twitter.TWITTER_OAUTH_AUTHORIZE
    return HttpResponseRedirect(url + '?oauth_token=' + token)

@require_GET
def twitter_oauth_complete(request):
    token = request.GET['oauth_token']
    verifier = request.GET['oauth_verifier']

    if token != request.session['temporary_oauth_token']:
        logger.warning("tokens don't match, do not move forward with authentication")
        return render(request, 'errors/500.html')

    secret = request.session['temporary_oauth_secret']

    client = twitter.Twitter(token, secret)
    data = client.generate_access_token(verifier)

    access_token = data['oauth_token']
    access_token_secret = data['oauth_token_secret']
    username = data['screen_name']
    id = data['user_id']

    # At this point, there are two things that could happen. Either there
    # is an existing user that needs to be tied to a Twitter account, or a
    # new user will be created.
    if request.user.is_authenticated():
        user = request.user
    else:
        app_label, model_name = settings.PRIMARY_USER_MODEL.split('.')
        GenericUser = get_model(app_label, model_name)
        user, created = GenericUser.objects.get_or_create(twitter_id=id)

    # Sweet. The user now has Twitter data. Redirect them home.
    # Middleware will take care of other redirects.
    user.twitter_username = username
    user.twitter_access_token = access_token
    user.twitter_access_token_secret = access_token_secret
    user.save()

    # Authenticate the user
    user = authenticate(access_token=access_token, access_token_secret=access_token_secret)
    if user:
        login(request, user)
    else:
        raise Exception

    signals.twitter_auth_completed.send(sender='ecl_twitter',
            access_token=access_token,
            access_token_secret=access_token_secret,
            username=username,
            id=id)

    return HttpResponseRedirect(reverse('home'))

