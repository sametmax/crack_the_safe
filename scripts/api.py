#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu


import sys
import urllib2
import json

api = json.loads(urllib2.urlopen(sys.argv[1]).read())

res = [(c, len(d)) for c, d in api.iteritems()]

res.sort(key=lambda e: e[1], reverse=True)

print ''.join(char for char, count in res[:10])
