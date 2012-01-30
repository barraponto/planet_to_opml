# -*- coding: utf-8 -*-
from lxml.html import parse
from opml import OPML

class DrupalPlanetOPML(OPML):
    def scrape(self, url):
        dom = parse(url).getroot()
        for line in dom.cssselect('#block-drupalorg_news-planet-list .item-list li'):
            links = line.cssselect('a')
            self.add_rss(
                    text=links[0].text_content(),
                    htmlUrl=links[0].get('href'), 
                    xmlUrl=links[1].get('href'),
                    )

def main():
    opml = DrupalPlanetOPML('Drupal Planet OPML')
    opml.scrape('http://drupal.org/planet')
    opml.write_file('drupal-planet.opml')

if __name__ == '__main__':
    main()
