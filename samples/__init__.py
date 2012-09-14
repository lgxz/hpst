#!/usr/bin/env python
#coding: utf-8

""" 样本数据获取接口 """

import os
import sys

__all__ = ['CSamplesHTML']


class CSamples():
    """ 样本数据基类 """
    def __init__(self):
        """Init """
        pass

    def __iter__(self):
        """Iter """
        raise StopIteration


class CSamplesHTML(CSamples):
    """ HTML 样本类 """
    def __init__(self, options):
        """Init """
        CSamples.__init__(self)

        self._options = options

        this_file = globals()['__file__']
        self.mydir = os.path.dirname(this_file)
        self.html_dir = os.path.join(self.mydir, 'html')
        self.html_files = os.listdir(self.html_dir)

        if options.skip > 0:
            self.html_files = self.html_files[options.skip:]


    def __iter__(self):
        """Iter """
        for filename in self.html_files:
            filepath = os.path.join(self.html_dir, filename)

            try:
                html = open(filepath, 'r').read()
            except Exception, e:
                print >> sys.stderr, "Failed to read from file: %s, error: %s" % (filename, str(e))
                continue

            try:
                html2 = html.decode('GBK').encode('UTF-8')
            except:
                html2 = html
                
            sample = {'filename': filename, 'content': html2}
            yield sample


if __name__ == '__main__':
    samples = CSamplesHTML()

    for sample in samples:
        print sample

