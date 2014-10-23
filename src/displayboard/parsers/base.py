# coding=utf-8
"""
"""
__author__ = 'Alisue <lambdalisue@hashnote.net>'


class BaseParser(object):
    def parse(self, text):
        raise NotImplementedError
