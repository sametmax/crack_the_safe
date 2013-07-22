#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu


import sys
import urllib2
import pickle
import base64

baseurl, payload = sys.argv[1:]

NextUrlContainer = type("NextUrlContainer", (), {'__init__': (lambda s, n: setattr(s, 'next', n))})

while True:
    res = pickle.loads(base64.decodestring(payload)).next
    print res
    try:
        payload = urllib2.urlopen(baseurl + '/%s' % res).read()
    except:
        break
