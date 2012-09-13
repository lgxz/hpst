#!/usr/bin/env python
#coding: utf-8

""" __init__ """

import os

from target_bs import CTargetBS
from target_lxml import CTargetLXML

__targets_class__ = [CTargetBS, CTargetLXML]


class CTargets():
    """ All targets """

    def __init__(self, options):
        """ init """
        self._options = options
        self._targets = [ obj(options) for obj in __targets_class__ ]


    def test(self, sample, results):
        """ Test Entry """
        for target in self._targets:
            target.test(sample, results)

