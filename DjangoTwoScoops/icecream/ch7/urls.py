# -*- coding: UTF-8 -*-
from django.views.generic import TemplateView
from ch7 import views

__author__ = 'ielkin'

from django.conf.urls import patterns, url

urlpatterns = patterns('',
                url(r'^$', TemplateView.as_view(template_name='base.html'), name='index'),
                url(r'^meta/$', views.meta, name='meta'),
                url(r'^date/(?P<month>\w{3})/(?P<day>\d\d)/$', views.date),
                (r'^date/birthday/$', views.date, {'month': 'Dec', 'day': '22'}),
)