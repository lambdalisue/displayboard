# coding=utf-8
"""
"""
__author__ = 'Alisue <lambdalisue@hashnote.net>'
import markdown2
from .base import BaseParser


class MarkdownParser(BaseParser):
    def parse(self, text):
        return markdown2.markdown(text)
