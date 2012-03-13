# -*- coding: utf-8 -*-
from lxml.html import parse
from opml import OPML

class KDEPlanetOPML(OPML):
    def scrape(self, url):
        dom = parse(url).getroot()
        for line in dom.cssselect('#feeds .feedsrow'):
            columns = line.cssselect('td')
            links = columns[0].cssselect('a')
            self.add_rss(
                    text=columns[0].text_content(),
                    htmlUrl=links[0].get('href') if links else '',
                    xmlUrl=columns[1].cssselect('a')[0].get('href'),
                    )

def main():
    opml = KDEPlanetOPML('KDE Planet OPML')
    opml.scrape('http://planet.kde.org/')
    opml.write_file('kde-planet.opml')

if __name__ == '__main__':
    main()
