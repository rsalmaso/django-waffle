# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals
from django.conf.urls import url
from waffle.views import wafflejs

urlpatterns = [
    url(r'^wafflejs$', wafflejs, name='wafflejs'),
]
