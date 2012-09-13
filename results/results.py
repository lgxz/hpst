#!/usr/bin/env python
#coding: utf-8

""" Test results """

from pprint import pprint


class CResults(dict):
    """ Test results """
    def __init__(self, options):
        """ init """
        self._options = options
        self._stats = {}


    def add(self, name, result, sample):
        """ Add a result record """
        stats = self._stats

        try:
            stat = stats[name]
        except:
            stat = {'ok': 0, 'err': 0, 'time': 0, 'size': 0}
            stats[name] = stat

        if self._options.verbose:
            try:
                content = str(result['time'])
            except:
                content = result['except']
            print '%s: %s -> %s' % (name, sample['filename'], content)

        if 'time' in result:
            stat['ok'] += 1
            stat['time'] += result['time']
            stat['size'] += len(sample['content'])
        else:
            stat['err'] += 1


    def show(self):
        """ Show results """
        pprint(self._stats)


