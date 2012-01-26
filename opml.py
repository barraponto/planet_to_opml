# -*- coding: utf-8 -*-
from lxml import etree
from scrape import feeds

root = etree.Element('opml')
root.set('version', '2.0')
head = etree.SubElement(root, 'head')
body = etree.SubElement(root, 'body')
for feed in feeds:
    outline = etree.SubElement(body, 'outline')
    outline.set('text', feed['title'])
    outline.set('type', 'rss')
    outline.set('htmlUrl', feed['section'])
    outline.set('xmlUrl', feed['feed'])

opml = open('drupal-planet.opml', 'w')
opml.write(etree.tostring(root, pretty_print=True, encoding='utf-8'))

