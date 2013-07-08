# -*- coding: UTF-8 -*-
from django.conf import settings
from django.views.generic import TemplateView
from ch5 import views

__author__ = 'ielkin'

from django.conf.urls import patterns, url

urlpatterns = patterns('ch5.views',
                       url(r'^$', TemplateView.as_view(template_name="base.html"), name='index'),
                       # Pass view as function
                       url(r'^search/$', views.search, name='search'),
                       # Pass view as name (see also prefix above)
                       url(r'^contact/$', 'contact', name='contact'),
                       url(r'^thanks/$', TemplateView.as_view(template_name="thanks.html"), name='thanks'),
                       url(r'^books/$', 'books_author', name='books_author'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^debuginfo/$', views.debug),
                            )