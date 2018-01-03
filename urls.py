from django.urls import include, path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from lionheart.utils import status_204

from app import views

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('204$', status_204),
    path('', views.home, name='home'),
]

urlpatterns += staticfiles_urlpatterns()

