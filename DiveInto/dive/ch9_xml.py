# -*- coding: UTF-8 -*-
__author__ = 'ielkin'

# Parsing
from xml.dom import minidom
xmldoc = minidom.parse('samples/kgp/binary.xml')
print xmldoc.toxml()

print xmldoc.lastChild.toxml()

# Traversing
grammarNode = xmldoc.lastChild
refNode = grammarNode.childNodes[1]
pNode = refNode.childNodes[1]
print pNode
print pNode.firstChild.data

# Search by name
refList = xmldoc.getElementsByTagName("ref")
print refList[0].toxml()

# Attributes
print refList[0].attributes.keys()
print refList[0].attributes.values()
print refList[0].attributes["id"].name
print refList[0].attributes["id"].value

# Unicode strings
import sys
print sys.getdefaultencoding()

xmldoc = minidom.parse('samples/kgp/russiansample.xml')
title = xmldoc.getElementsByTagName('title')[0].firstChild.data
print title

s = u'Игорь'
print s