import logging

from django.shortcuts import get_object_or_404

from ecl_django.decorators import render

logger = logging.getLogger(__name__)

@render
def home(request):
    return {}

