import sys


def main():
    RSReader().main(sys.argv)


class RSReader(object):
    xkcd_items = \
        """Wed, 05 Dec 2007 05:00:00 -0000: xkcd.com: Python\nMon, 03 Dec 2007 05:00:00 -000: xkcd.com: Far Away"""

    def main(self, argv):
        if argv[1:]:
            print(self.xkcd_items)

    def listing_from_item(self, feed, item):
        subst = (item['date'], feed['feed']['title'], item['title'])
        return "%s: %s: %s" % subst

    def feed_listing(self, feed):
        item_listings = [self.listing_from_item(feed, x) for x in feed['entries']]
        return "\n".join(item_listings)


if __name__ == '__main__':
    sys.exit(main())
