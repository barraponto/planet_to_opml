# -*- coding: utf-8 -*-
from lxml.html import parse
from urlparse import urlparse
from opml import OPML

feeds = []
dom = parse('http://drupal.org/planet').getroot()

for line in dom.cssselect('#block-drupalorg_news-planet-list .item-list li'):
    links = line.cssselect('a')
    feeds.append({
        'text': links[0].text_content(),
        'htmlUrl': links[0].get('href'), 
        'xmlUrl': links[1].get('href'),
    })

def main():
    opml = OPML('Drupal Planet OPML', feeds)
    file = open('drupal-planet.opml', 'w')
    file.write(etree.tostring(opml.root, pretty_print=True, encoding='utf-8'))

if __name__ == '__main__':
    main()
