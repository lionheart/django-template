from datetime import datetime
import json
import re

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core.mail import EmailMultiAlternatives
from django.db.models import Sum, Q, F
from django.conf import settings
from django.db import models
from django.db import transaction
from django.template.defaultfilters import slugify
from django.template.loader import render_to_string
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from lionheart.models import CreatedMixin

class UserQuerySet(models.QuerySet):
    pass


class UserManager(BaseUserManager):
    def create_superuser(self, email, password, **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)


class User(AbstractBaseUser, CreatedMixin):
    USERNAME_FIELD = "email"

    email = models.EmailField(max_length=80, unique=True)

    objects = UserManager()

    @property
    def is_staff(self):
        return True

    @property
    def is_active(self):
        return True

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_perms(self, perm):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

