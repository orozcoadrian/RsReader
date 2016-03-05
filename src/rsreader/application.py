import sys


def main():
    xkcd_items = \
        """Wed, 05 Dec 2007 05:00:00 -0000: xdkc.com: Python
        Mon, 03 Dec 2007 05:00:00 -000: xkcd.com: Far Away"""
    if len(sys.argv) == 2:
        print(xkcd_items)


if __name__ == '__main__':
    sys.exit(main())
