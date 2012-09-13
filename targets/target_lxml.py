#!/usr/bin/env python
#coding: utf-8

""" Test Target: lxml """

import lxml.html

from target import CTarget


class CTargetLXML(CTarget):
    name = 'lxml'
    version = '2.3.4'

    def _test(self, sample):
        """ Actual Test Enrty """
        html = sample['content']
        elapsed = self.timeit(lambda: lxml.html.fromstring(html))
        return {'time': elapsed}

