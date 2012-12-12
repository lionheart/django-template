from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse

from aurora.utils import simple_url
from aurora.utils import template_url
from aurora.utils import home_url
from aurora.utils import status_204

admin.autodiscover()

urlpatterns = patterns('app.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^204$', status_204),
    home_url('home'),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

