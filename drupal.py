# -*- coding: utf-8 -*-
from urlparse import urlparse
from lxml.html import parse
from lxml import etree
from opml import OPML

def main():
    opml = OPML('Drupal Planet OPML')
    dom = parse('http://drupal.org/planet').getroot()
    for line in dom.cssselect('#block-drupalorg_news-planet-list .item-list li'):
        links = line.cssselect('a')
        opml.add_rss(
                text=links[0].text_content(),
                htmlUrl=links[0].get('href'), 
                xmlUrl=links[1].get('href'),
                )
    file = open('drupal-planet.opml', 'w')
    file.write(etree.tostring(opml.root, pretty_print=True, encoding='utf-8'))

if __name__ == '__main__':
    main()
