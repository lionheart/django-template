from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse

from ecl_django.utils import simple_url
from ecl_django.utils import template_url
from ecl_django.utils import home_url
from ecl_django.utils import status_204

admin.autodiscover()

urlpatterns = patterns('app.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^204$', status_204),
    home_url('home'),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

