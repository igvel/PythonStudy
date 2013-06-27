from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),

    # Examples:
    # url(r'^$', 'icecream.views.home', name='home'),
    # url(r'^icecream/', include('icecream.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #"Django Book" Apps URLs:
    url(r'^ch3/', include('ch3.urls', namespace="ch3")),
    url(r'^ch4/', include('ch4.urls', namespace="ch4")),
    url(r'^ch5/', include('ch5.urls', namespace="ch5")),
    url(r'^ch7/', include('ch7.urls', namespace="ch7")),
)
