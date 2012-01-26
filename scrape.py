# -*- coding: utf-8 -*-
from lxml.html import parse
from urlparse import urlparse

feeds = []
dom = parse('http://drupal.org/planet').getroot()

for line in dom.cssselect('#block-drupalorg_news-planet-list .item-list li'):
    links = line.cssselect('a')
    feeds.append({
        'title': links[0].text_content(),
        'section': links[0].get('href'), 
        'feed': links[1].get('href'),
    })

