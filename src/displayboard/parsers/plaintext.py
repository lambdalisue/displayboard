# coding=utf-8
"""
"""
__author__ = 'Alisue <lambdalisue@hashnote.net>'
from .base import BaseParser


class PlainTextParser(BaseParser):
    def parse(self, text):
        return text
