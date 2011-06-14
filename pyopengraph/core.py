#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Copyright (c) 2010 Gerson Minichiello
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

import rdfadict

OPENGRAPH_NAMESPACES = [
  "http://opengraphprotocol.org/schema",
  "http://opengraphprotocol.org/schema/",
  "http://ogp.me/ns#",
]

class PyOpenGraph(object):
   
    def __init__(self, url=None, xml=None):
        parser = rdfadict.RdfaParser()
        if not xml:
            result = parser.parse_url(url)
        else:
            result = parser.parse_string(xml, url)
        data = result[url]
        self.metadata = self.get_properties(data)

    def get_properties(self, data):
        content = {}
        for k, v in data.iteritems():
            for ns in OPENGRAPH_NAMESPACES:
                if k.startswith(ns) and len(v)>0:
                    content[k.replace(ns, '')] = v[0]
        return content
    
    def __str__(self):
        return self.metadata['title']

if __name__ == '__main__':
    # Usage
    og = PyOpenGraph('http://www.zappos.com/timberland-pro-titan-safety-toe-oxford')
    print og.metadata
