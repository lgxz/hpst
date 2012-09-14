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
        self._redis = options.redis


    def add(self, name, result, sample):
        """ Add a result record """
        stats = self._stats

        try:
            stat = stats[name]
        except:
            stat = {'ok': 0, 'err': 0, 'time': 0, 'size': 0}
            stats[name] = stat

        if 'time' in result:
            if self._options.verbose:
                print '%s: %s -> %u' % (name, sample['filename'], result['time'])

            stat['ok'] += 1
            stat['time'] += result['time']
            stat['size'] += len(sample['content'])
        else:
            stat['err'] += 1
            print '%s: %s -> %s' % (name, sample['filename'], result['except'])

        if self._redis:
            self._redis.hmset(name, stat)


    def show(self):
        """ Show results """
        pprint(self._stats)


