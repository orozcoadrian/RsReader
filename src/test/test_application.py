from unittest import TestCase
import sys
from io import StringIO

from rsreader.application import main


class AcceptanceTests(TestCase):
    def setUp(self):
        self.old_value_of_stdout = sys.stdout
        sys.stdout = StringIO()
        self.old_value_of_argv = sys.argv

    def tearDown(self):
        sys.stdout = self.old_value_of_stdout
        sys.argv = self.old_value_of_argv

    def test_should_get_one_URL_and_print_output(self):
        printed_items = \
            """Wed, 05 Dec 2007 05:00:00 -0000: xdkc.com: Python
            Mon, 03 Dec 2007 05:00:00 -000: xkcd.com: Far Away"""

        sys.argv = ["unused_prog_name", "xkcd.rss.xml"]
        main()
        self.assertEquals(printed_items + "\n",
                          sys.stdout.getvalue())

    def test_no_urls_should_print_nothing(self):
        sys.argv = ["unused_prog_name"]
        main()
        self.assertEquals("", sys.stdout.getvalue())

    def test_many_urls_should_print_first_results(self):
        printed_items = \
            """Wed, 05 Dec 2007 05:00:00 -0000: xdkc.com: Python
            Mon, 03 Dec 2007 05:00:00 -000: xkcd.com: Far Away"""

        sys.argv = ["unused_prog_name", "xkcd.rss.xml", "excess"]
        main()
        self.assertEquals(printed_items + "\n",
                          sys.stdout.getvalue())
