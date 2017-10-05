from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from lionheart.utils import simple_url
from lionheart.utils import template_url
from lionheart.utils import home_url
from lionheart.utils import status_204

from app import views

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^204$', status_204),
    home_url(views.home),
]

urlpatterns += staticfiles_urlpatterns()

