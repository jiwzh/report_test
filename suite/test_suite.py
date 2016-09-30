# -*- coding: utf-8 -*-

import unittest
import serial
from myexcel import myexcel
from mycom import mycom
from time import sleep

class Test_LKJ(unittest.TestCase):
    def setUp(self):
        print "setup"
        