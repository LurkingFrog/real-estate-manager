from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Enable the admin. As the product grows, this should eventually
# be deprecated
admin.autodiscover()


urlpatterns = patterns(
    'apps.main.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^datatables/', include('data_tables.urls')),

    url(r'^$', 'landing_page', name='landing_page'),
    url(r'^agents$', 'agents', name='agent_totals'),
)


urlpatterns += staticfiles_urlpatterns()
