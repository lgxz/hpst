#!/usr/bin/env python
#coding: utf-8

""" Test Target: BeautifulSoup """

from bs4 import __version__ as VERSION
from bs4 import BeautifulSoup

from target import CTarget


class CTargetBS(CTarget):
    name = 'BeautifulSoup'
    version = VERSION

    def _test(self, sample):
        """ Actual Test Enrty """
        html = sample['content']
        elapsed = self.timeit(lambda: BeautifulSoup(html, from_encoding="UTF-8"))
        return {'time': elapsed}

