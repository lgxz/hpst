#!/usr/bin/env python
#coding: utf-8

""" Test Target: BeautifulSoup """

from BeautifulSoup import BeautifulSoup

from target import CTarget


class CTargetBS(CTarget):
    name = 'BeautifulSoup'
    version = '3.2.0'

    def _test(self, sample):
        """ Actual Test Enrty """
        html = sample['content']
        elapsed = self.timeit(lambda: BeautifulSoup(html, fromEncoding="UTF-8"))
        return {'time': elapsed}

