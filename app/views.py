import logging
import random

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import *
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

from decorators import unauthenticated_users_only
from forms import *

from goodiebag.utils import twitter, facebook

logger = logging.getLogger(__name__)

def home(request):
    pass

def login_page(request):
    pass

def logout_page(request):
    pass

def register_page(request):
    pass

