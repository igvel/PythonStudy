# -*- coding: UTF-8 -*-
__author__ = 'ielkin'

import unittest


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEquals(1, 1)

if __name__ == '__main__':
    unittest.main()
