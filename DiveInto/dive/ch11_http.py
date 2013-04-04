# -*- coding: UTF-8 -*-
__author__ = 'ielkin'

import httplib
httplib.HTTPConnection.debuglevel = 1
proxies = {'http': 'http://172.20.64.254:8080'}
#import urllib
#feeddata = urllib.urlopen('http://diveintomark.org/xml/atom.xml', proxies=proxies).read()
import urllib2
proxyHandler = urllib2.ProxyHandler(proxies)
url = 'http://diveintomark.org/xml/atom.xml'
request = urllib2.Request(url)
opener = urllib2.build_opener(proxyHandler)
feeddata = opener.open(request).read()
print feeddata

print request.get_full_url()
request.add_header('User-Agent', 'IVEL/1.0')
feeddata = opener.open(request).read()
print feeddata

import urlparse
print urlparse.urlparse(url)

import samples.openanything

result = samples.openanything.fetch(url)
print result