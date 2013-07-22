#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu

import os
import sys

from zipfile import ZipFile

os.chdir(os.path.dirname(os.path.realpath(sys.argv[1])))

for x in xrange(1, 9999, 1):

    print "Unzipping %s" % 'one_more_time_%s.zip' % x
    with ZipFile('one_more_time_%s.zip' % x) as myzip:
        try:
            with open('one_more_time_%s.zip' % (x + 1), 'w') as f:
                f.write(myzip.open('one_more_time_%s.zip' % (x + 1)).read())
                os.remove('one_more_time_%s.zip' % x)
        except:
            break


