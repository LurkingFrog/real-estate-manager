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

    url(r'^agents$', 'agents', name='agents'),
    url(r'^agent/(?P<agent_id>\d+)$', 'agent_details', name='agent_details'),
    url(r'^manage/agent/new$', 'manage_agent', name='add_agent'),
    url(r'^manage/agent/(?P<agent_id>\d+)$', 'manage_agent', name='view_agent'),

    url(r'^listings$', 'listings', name='listings'),

    url(r'^commissions$', 'commissions', name='commissions'),

    url(r'^closings$', 'closings', name='closings'),
    
)

urlpatterns += staticfiles_urlpatterns()
