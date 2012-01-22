from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
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

# XXX Uncomment for Facebook integration
# import ecl_facebook
#
# urlpatterns += patterns('ecl_facebook.views',
#     url(r'oauth/facebook/begin$', 'oauth_facebook_begin', name='oauth-facebook-begin'),
# )

if settings.DEBUG:
    urlpatterns += (
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT }),
        )

