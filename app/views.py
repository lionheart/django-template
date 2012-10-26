import logging

from django.shortcuts import get_object_or_404

from plus.decorators import render

logger = logging.getLogger(__name__)

@render
def home(request):
    return {}

