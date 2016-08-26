#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-08-25 12:18:37

from tieba.models import *
from django.contrib.auth.models import User
from tieba.serializers import *
from snippets.serializers import *

wx = User.objects.get(username='wangx')
a = Album.objects.first()
t = Track.objects.first()
