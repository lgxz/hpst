#!/usr/bin/env python
#coding: utf-8

""" Test Target """

from datetime import datetime


class CTarget():
    name = None
    version = None

    def __init__(self, options):
        """ Init """
        self._options = options


    def timeit(self, func):
        """ Timeit """
        time_start = datetime.now()
        obj = func()
        delta = datetime.now() - time_start

        del obj
        total = delta.seconds*1000000 + delta.microseconds
        return total


    def test(self, sample, result):
        """ Test Entry """
        try:
            _result = self._test(sample)
        except Exception, e:
            _result = {'except': str(e)}

        result.add('%s/%s' % (self.name, self.version), _result, sample)


    def _test(self, sample):
        """ Actual Test Enrty """
        raise Exception('Override ME')


