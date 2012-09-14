#!/usr/bin/env python
#coding: utf-8

""" Test Target: lxml """

import lxml.html
from lxml import etree

from target import CTarget


class CTargetLXML(CTarget):
    name = 'lxml'
    version = '2.3.5'

    def _test(self, sample):
        """ Actual Test Enrty """
        etree.clear_error_log()
        html = sample['content']
        elapsed = self.timeit(lambda: lxml.html.fromstring(html))
        return {'time': elapsed}

