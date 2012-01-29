# -*- coding: utf-8 -*-
from lxml import etree
from scrape import feeds

class OPML:
    def __init__(self, title=False, outlines=[]):
        self.root = etree.Element('opml', version='2.0')
        self.head = etree.SubElement(self.root, 'head')
        self.body = etree.SubElement(self.root, 'body')
        if isinstance(title, basestring):
            self.title = title
            etree.SubElement(self.head, 'title').text = self.title
        for outline in outlines:
            etree.SubElement(
                    self.body, 'outline', text=outline['text'], type='rss',
                    htmlUrl=outline['htmlUrl'], xmlUrl=outline['xmlUrl'])


def main():
    opml = OPML('Drupal Planet OPML', feeds)
    file = open('drupal-planet.opml', 'w')
    file.write(etree.tostring(opml.root, pretty_print=True, encoding='utf-8'))

if __name__ == '__main__':
    main()
