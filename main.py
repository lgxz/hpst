#!/usr/bin/env python
#coding: utf-8

""" Main module """

import signal

import samples
import results
import targets
from options import COptions


m_stop = False


def on_sigint(signo, frame):
    """ SIGINT handler """
    global m_stop

    m_stop = True


def init_options():
    """ Init options """
    options = COptions()

    return options


def main():
    """ Program entry """
    options = init_options()

    _samples = samples.CSamplesHTML(options)
    _results = results.CResultsHTML(options)
    _targets = targets.CTargets(options)

    signal.signal(signal.SIGINT, on_sigint)

    for _sample in _samples:
        _targets.test(_sample, _results)
        if m_stop:
            break

    _results.show()


if __name__ == '__main__':
    main()

