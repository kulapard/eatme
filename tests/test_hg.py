# -*- coding: utf-8 -*-
import unittest

from eatme import hg


class TestHG(unittest.TestCase):
    def test_status(self):
        self.assertIsNone(hg.status(path='.'))

    def test_branch(self):
        self.assertIsNone(hg.branch(path='.'))


if __name__ == '__main__':
    unittest.main()
