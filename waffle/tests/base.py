# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals
from django import test
from django.core import cache


class TestCase(test.TransactionTestCase):

    def _pre_setup(self):
        cache.cache.clear()
        super(TestCase, self)._pre_setup()
