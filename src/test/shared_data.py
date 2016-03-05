import os

__all__ = ['expected_items', 'printed_items']
expected_items = [
    "Wed, 05 Dec 2007 05:00:00 -0000: xkcd.com: Python",
    "Mon, 03 Dec 2007 05:00:00 -0000: xkcd.com: Far Away"
]
printed_items = os.linesep.join(expected_items)
