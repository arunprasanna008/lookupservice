#!/usr/bin/env python3

import unittest
from main import CheckUrl

class TestCheckUrl(unittest.TestCase):

    def setUp(self):
        self.service = CheckUrl()

    def test_get_ok(self):
        print(self.service.get('/urlinfo/1/'))

    def test_get_bad(self):
        print(self.service.get(''))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()