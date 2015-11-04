# -*- coding: utf-8 -*-
import unittest

from eatme import EatMe, run_for_all_repos
from testfixtures import log_capture


class TestEatMe(unittest.TestCase):
    @log_capture()
    def test_run(self, l):
        self.assertTrue(callable(EatMe.run))

    def test_run_for_all_repos(self):
        def func(path):
            self.assertIsInstance(path, str)

        self.assertTrue(callable(run_for_all_repos))
        self.assertIsNone(run_for_all_repos(func))

if __name__ == '__main__':
    unittest.main()
