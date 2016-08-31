#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-08-16 16:32:02

from django.conf.urls import url
from tieba import views


urlpatterns = [
    url(r'^post/$', views.PostList.as_view(), name='tieba-list'),
    url(r'^post/(?P<pk>[0-9]+)/$',
        views.PostDetailView.as_view(), name='groupdetail'),
]
