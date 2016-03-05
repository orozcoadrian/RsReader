from nose.tools import *
import feedparser

from rsreader.application import RSReader
from test.shared_data import *

items = [{'date': "Wed, 05 Dec 2007 05:00:00 -0000",
          'title': "Python"},
         {'date': "Mon, 03 Dec 2007 05:00:00 -0000",
          'title': "Far Away"}]
feed = {'feed': {'title': "xkcd.com"}, 'entries': items}


def test_listing_from_item():
    computed_line = RSReader().listing_from_item(feed, items[0])
    assert_equals(expected_items[0], computed_line)


def test_feed_listing():
    computed_line = RSReader().feed_listing(feed)
    assert_equals(printed_items, computed_line)


def test_feed_from_url():
    url = "http://www.xkcd.com/rss.xml"

    def parse_stub(url):
        return feed

    real_parse = feedparser.parse
    feedparser.parse = parse_stub
    try:
        assert_equals(feed, RSReader().feed_from_url(url))
    finally:
        feedparser.parse = real_parse
