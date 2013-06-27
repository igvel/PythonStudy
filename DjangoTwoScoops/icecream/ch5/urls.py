# -*- coding: UTF-8 -*-
from django.views.generic import TemplateView
from ch5 import views

__author__ = 'ielkin'

from django.conf.urls import patterns, url

urlpatterns = patterns('',
                url(r'^$', TemplateView.as_view(template_name="base.html"), name='index'),
                url(r'^search/$', views.search, name='search'),
                url(r'^contact/$', views.contact, name='contact'),
                url(r'^thanks/$', TemplateView.as_view(template_name="thanks.html"), name='thanks'),
)