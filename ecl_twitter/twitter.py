import random
import time
import hmac
import hashlib
import urllib
import urlparse
import httplib

from django.conf import settings
from operator import itemgetter

TWITTER_BASE_URL = 'https://api.twitter.com'
TWITTER_INSECURE_URL = 'http://api.twitter.com'
TWITTER_OAUTH_REQUEST = '/oauth/request_token'
TWITTER_OAUTH_AUTHORIZE = '/oauth/authorize'
TWITTER_OAUTH_ACCESS_TOKEN = '/oauth/access_token'

generate_sorted_params = lambda k: sorted(k.iteritems(), key=itemgetter(0))
generate_timestamp = lambda: str(int(time.time()))
generate_nonce = lambda: hashlib.sha1(str(random.random())).hexdigest()

PARAMS = lambda: {
    'oauth_nonce': generate_nonce(),
    'oauth_timestamp': generate_timestamp(),
    'oauth_consumer_key': settings.TWITTER_CONSUMER_KEY,
    'oauth_signature_method': 'HMAC-SHA1',
    'oauth_version': '1.0'
}

encode_tuple = lambda k, v: urllib.quote(k) + '%3D' + urllib.quote(urllib.quote(v, safe=''))

def generate_base_string(method, url, params):
    sorted_params = generate_sorted_params(params)
    encoded_params = '%26'.join([encode_tuple(k, v) for k, v in sorted_params])
    return '&'.join([method, urllib.quote_plus(url), encoded_params])

def generate_signature(base_string, oauth_token_secret=None):
    signing_key = settings.TWITTER_CONSUMER_SECRET + '&'
    if oauth_token_secret:
        signing_key += oauth_token_secret

    hash = hmac.new(signing_key, base_string, hashlib.sha1)
    return hash.digest().encode('base-64')[:-1]

class Twitter():
    def __init__(self, token=None, secret=None, ssl=True):
        self.token = token
        self.secret = secret
        self.ssl = ssl

    def get(self, resource, params=None):
        return self.oauth_response('GET', resource, params)

    def post(self, resource, params=None):
        return self.oauth_response('POST', resource, params)

    def generate_access_token(self, pin):
        params = {'oauth_verifier': pin}
        response = self.get(TWITTER_OAUTH_ACCESS_TOKEN, params)
        return dict(urlparse.parse_qsl(response.read()))

    def generate_authorization_url(self, callback=None):
        if callback:
            params = {'oauth_callback': callback}
        else:
            params = {'oauth_callback': settings.TWITTER_CALLBACK_URL}

        response = self.get(TWITTER_OAUTH_REQUEST, params)

        data = dict(urlparse.parse_qsl(response.read()))
        return data

    def oauth_response(self, method, resource, params={}, oauth_params=None):
        if self.ssl:
            conn = httplib.HTTPSConnection('api.twitter.com')
            url = TWITTER_BASE_URL
        else:
            conn = httplib.HTTPConnection('api.twitter.com')
            url = TWITTER_INSECURE_URL
        url += resource

        signing_params = PARAMS()
        signing_params.update(params)

        if self.token:
            signing_params['oauth_token'] = self.token

        base_string = generate_base_string(method, url, signing_params)

        header_params = {}
        query_params = {}
        for key, value in signing_params.iteritems():
            if key.startswith("oauth_"):
                header_params[key] = urllib.quote(value, safe='')
            else:
                query_params[key] = urllib.quote(value)

        signature = generate_signature(base_string, self.secret)
        header_params['oauth_signature'] = urllib.quote_plus(signature)
        auth_string = 'OAuth realm="", %s' % ', '.join(['%s="%s"' % (k, v)
            for k, v in header_params.iteritems()])

        if params:
            encoded_params = "&".join("%s=%s" % (k, v) for k, v in query_params.iteritems())

        if method == 'POST':
            conn.request(method, resource, encoded_params, {'Authorization': auth_string})
        else:
            conn.request(method, resource + "?" + encoded_params, headers={'Authorization': auth_string})

        response = conn.getresponse()
        return response


