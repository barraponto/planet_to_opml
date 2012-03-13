# -*- coding: utf-8 -*-
from lxml.html import parse
from opml import OPML

class jQueryPlanetOPML(OPML):
    def scrape(self, url):
        dom = parse(url).getroot()
        for line in dom.cssselect('#sidebar > ul > li > a'):
            self.add_rss(
                    text=line.text_content(),
                    htmlUrl=line.get('href'), 
                    )

def main():
    opml = jQueryPlanetOPML('jQuery Planet OPML')
    opml.scrape('http://planet.jquery.com/')
    opml.write_file('jquery-planet.opml')

if __name__ == '__main__':
    main()
