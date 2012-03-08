from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

# Enable the admin. As the product grows, this should eventually
# be deprecated
admin.autodiscover()

urlpatterns = patterns(
    'apps.main.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'landing_page', name='landing_page')
)

