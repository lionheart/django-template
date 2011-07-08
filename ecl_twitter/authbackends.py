from django.conf import settings
from django.db.models import get_model

app_label, model_name = settings.PRIMARY_USER_MODEL.split('.')
GenericUser = get_model(app_label, model_name)

class TwitterBackend():
    def authenticate(self, access_token, access_token_secret):
        try:
            return GenericUser.objects.get(twitter_access_token=access_token,
                    twitter_access_token_secret=access_token_secret)
        except GenericUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return GenericUser.objects.get(pk=user_id)
        except GenericUser.DoesNotExist:
            return None

