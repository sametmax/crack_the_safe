#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu

import os

from zipfile import ZipFile

os.chdir(os.path.dirname(os.path.realpath(__file__)))

previous = "youdiditjonhy.txt"

for x in xrange(1000, 0, -1):

    print "Zipping %s" % previous
    with ZipFile('one_more_time_%s.zip' % x, 'w') as myzip:
        myzip.write(previous)
    if 'zip' in previous:
        os.remove(previous)
    previous = 'one_more_time_%s.zip' % x
