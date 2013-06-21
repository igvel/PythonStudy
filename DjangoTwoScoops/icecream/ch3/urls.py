# -*- coding: UTF-8 -*-
from ch3 import views

__author__ = 'ielkin'

from django.conf.urls import patterns, url

urlpatterns = patterns('',
                url(r'^$', views.hello, name='index'),
                url(r'^hello/$', views.hello, name='hello'),
                url(r'^time/plus/(\d{1,2})$', views.hours_ahead, name='time_plus'),
)