import logging

from django.shortcuts import get_object_or_404

from ecl_django.decorators import render

logger = logging.getLogger(__name__)

@render
def home(request):
    return {}

# XXX Uncomment for Facebook integration
# from ecl_facebook.decorators import facebook_callback
# from ecl_facebook.facebook import Facebook
# @facebook_callback
# def oauth_facebook_complete(request, token):
#     fb = Facebook(token)
#     fb_user = fb.me()
#     user = authenticate(id=fb_user.id)
#     login(request, user)
#     return HttpResponseRedirect(user.get_absolute_url())

