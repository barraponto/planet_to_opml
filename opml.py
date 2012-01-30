# -*- coding: utf-8 -*-
from lxml import etree

class OPML:
    def __init__(self, title=False, outlines=[]):
        self.root = etree.Element('opml', version='2.0')
        self.head = etree.SubElement(self.root, 'head')
        self.body = etree.SubElement(self.root, 'body')
        if isinstance(title, basestring):
            self.title = title
            etree.SubElement(self.head, 'title').text = self.title
        for outline in outlines:
            self.add_rss(**outline)

    def add_rss(self, **attributes):
        outline = etree.SubElement(self.body, 'outline', type='rss')
        for attribute in attributes:
            value = attributes[attribute]
            outline.set(attribute, value)

    def write_file(self, path):
        file = open(path, 'w')
        file.write(etree.tostring(self.root, pretty_print=True, encoding='utf-8'))
