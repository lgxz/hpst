#!/usr/bin/env python
#coding: utf-8

""" Main module """

import signal

import redis

import samples
import results
import targets
from options import COptions


m_stop = False


def on_sigint(signo, frame):
    """ SIGINT handler """
    global m_stop

    m_stop = True


def init_options(opts, args):
    """ Init options """
    options = COptions()

    options.redis = redis.Redis()
    options.skip = opts.skip

    return options


def parse_cmdline():
    """ cmd parse """
    from optparse import OptionParser

    parser = OptionParser(usage="usage: %prog [options]")

    parser.add_option('--skip', type=int, default=0, help='Skip first N samples')

    opts, args = parser.parse_args()
    return opts, args


def main():
    """ Program entry """
    opts, args = parse_cmdline()
    options = init_options(opts, args)

    _samples = samples.CSamplesHTML(options)
    _results = results.CResultsHTML(options)
    _targets = targets.CTargets(options)

    signal.signal(signal.SIGINT, on_sigint)

    for _sample in _samples:
        _targets.test(_sample, _results)
        del _sample
        if m_stop:
            break

    _results.show()


if __name__ == '__main__':
    main()

