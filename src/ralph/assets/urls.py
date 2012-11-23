#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.conf.urls.defaults import patterns
from django.contrib.auth.decorators import login_required

from ralph.assets.views import Index, AddDeviceAssets, AddPartAssets


urlpatterns = patterns(
    '', (r'^$', login_required(Index.as_view())),
    (r'^devices/add/', login_required(AddDeviceAssets.as_view())),
    (r'^part/add/', login_required(AddPartAssets.as_view())),
)
