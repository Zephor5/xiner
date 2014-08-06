from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', 'xiner.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^set_timezone', 'xiner.views.set_timezone', name='TimezoneSetting' ),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^members/', 'members.views.all', name='all')
)
