#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import django_rq

from ralph.inkpy import Converter


def convert(source_path, output_path, data):
    conv = Converter(source_path, output_path, data)
    conv.convert()


def run_async(source_path, output_path, data):
    queue = django_rq.get_queue('inkpy')

    return queue.enqueue_call(
        func=convert,
        args=(
            source_path,
            output_path,
            data,
        ),
        timeout=600,
    ).id
