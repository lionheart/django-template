from django.dispatch import Signal

twitter_auth_started = Signal(providing_args=[])
twitter_auth_completed = Signal(providing_args=['access_token', \
        'access_token_secret', 'username', 'id'])

