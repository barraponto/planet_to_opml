Planet OPML Generator
=====================

This is a very simple script that generates OPML files from Planets (those feed aggregators every free and open source project uses to show off its communities posts). It uses lxml to scrape the Planet page and build a XML file with the OPML format. See http://dev.opml.org/spec2.html for more on OPML.

How To
======

There are a few implementations I'm currently using in lieu of proper documentation. I know, I should have documented it properly, I'll get around to it, mind this is my first published python script (outside of ScraperWiki).

Basically, I'll you have to do is extend the `OPML` class and define a `scrape` method that adds rss to the OPML object using the `add_rss` method. Then just create your OPML object and call the `write_file` method.
