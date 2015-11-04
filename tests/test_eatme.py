# -*- coding: utf-8 -*-
import unittest

from eatme import EatMe
from testfixtures import log_capture


class TestEatMe(unittest.TestCase):
    @log_capture()
    def test_run(self, l):
        self.assertTrue(callable(EatMe.run))


if __name__ == '__main__':
    unittest.main()
