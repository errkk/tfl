from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tfl.views.home', name='home'),
    # url(r'^tfl/', include('tfl.foo.urls')),

    
    url(r'^admin/', include(admin.site.urls)),
)
