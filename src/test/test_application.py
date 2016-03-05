from nose.tools import *

from rsreader.application import RSReader
from test.shared_data import *

def test_listing_from_item():
    expected_line = """Wed, 05 Dec 2007 05:00:00 -0000: xkcd.com: Python"""
    item = {'date': "Wed, 05 Dec 2007 05:00:00 -0000",
            'title': "Python"}
    feed = {'feed': {'title': "xkcd.com"}}
    computed_line = RSReader().listing_from_item(feed, item)
    assert_equals(expected_line, computed_line)


def test_feed_listing():
    items = [{'date': "Wed, 05 Dec 2007 05:00:00 -0000",
              'title': "Python"},
             {'date': "Mon, 03 Dec 2007 05:00:00 -0000",
              'title': "Far Away"}]
    feed = {'feed': {'title': "xkcd.com"}, 'entries': items}
    computed_line = RSReader().feed_listing(feed)
    assert_equals(printed_items, computed_line)
