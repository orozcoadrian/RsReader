import os

__all__ = ['expected_items', 'printed_items', 'xkcd_rss_xml']
expected_items = [
    "Wed, 05 Dec 2007 05:00:00 -0000: xkcd.com: Python",
    "Mon, 03 Dec 2007 05:00:00 -0000: xkcd.com: Far Away"
]
printed_items = os.linesep.join(expected_items)

xkcd_rss_xml = '''<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0">
    <channel>
        <title>xkcd.com</title>
        <link>http://xkcd.com/</link>
        <description>xkcd.com: A webcomic of romance and math humor.</description>
        <language>en</language>
        <item>
            <title>Python</title>
            <link>http://xkcd.com/353/</link>
            <description>&lt;img src="http://imgs.xkcd.com/comics/python.png" title="I wrote 20 short programs in Python
                yesterday. It was wonderful. Perl, I'm leaving you." alt="I wrote 20 short programs in Python yesterday.
                It was wonderful. Perl, I'm leaving you." /&gt;</description>
            <pubDate>Wed, 05 Dec 2007 05:00:00 -0000</pubDate>
            <guid>http://xkcd.com/353/</guid>
        </item>
        <item>
            <title>Far Away</title>
            <link>http://xkcd.com/352/</link>
            <description>&lt;img src="http://imgs.xkcd.com/comics/far_away.png" title="Sometimes an impulsive 2:00 AM
                cross-country trip is the only solution." alt="Sometimes an impulsive 2:00 AM cross-country trip is the
                only solution." /&gt;</description>
            <pubDate>Mon, 03 Dec 2007 05:00:00 -0000</pubDate>
            <guid>http://xkcd.com/352/</guid>
        </item>
    </channel>
</rss>
'''
