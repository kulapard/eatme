# -*- coding: utf-8 -*-
import unittest

from plumbum import local
from eatme import hg


class TestHG(unittest.TestCase):
    TEST_REPO = 'https://bitbucket.org/KulaPard/pretty-hg'
    TEST_PATH = '/tmp/test_eatme_hg'

    def setUp(self):
        mkdir = local['mkdir']
        hg_clone = local['hg']['clone'][self.TEST_REPO][self.TEST_PATH]
        mk_test_path = mkdir[self.TEST_PATH]
        mk_test_path(retcode=[0, 1])
        hg_clone()

    def tearDown(self):
        rm = local['rm']
        rm_test_path = rm['-r', self.TEST_PATH]
        rm_test_path()

    def test_pull_update(self):
        self.assertIsNone(hg.pull_update(path=self.TEST_PATH))
        self.assertIsNone(hg.pull_update(path=self.TEST_PATH, branch='some_branch'))
        self.assertIsNone(hg.pull_update(path=self.TEST_PATH, clean=True))
        self.assertIsNone(hg.pull_update(path=self.TEST_PATH, branch='some_branch', clean=True))
        self.assertIsNone(hg.pull_update(path='/fake_path'))

    def test_push(self):
        self.assertIsNone(hg.push(path=self.TEST_PATH))
        self.assertIsNone(hg.push(path=self.TEST_PATH, branch='some_branch'))
        self.assertIsNone(hg.push(path=self.TEST_PATH, new_branch=True))
        self.assertIsNone(hg.push(path=self.TEST_PATH, branch='some_branch', new_branch=True))
        self.assertIsNone(hg.push(path='/fake_path'))

    def test_status(self):
        self.assertIsNone(hg.status(path=self.TEST_PATH))
        self.assertIsNone(hg.status(path='/fake_path'))

    def test_branch(self):
        self.assertIsNone(hg.branch(path=self.TEST_PATH))
        self.assertIsNone(hg.branch(path='/fake_path'))


if __name__ == '__main__':
    unittest.main()
