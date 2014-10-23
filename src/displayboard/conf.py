# coding=utf-8
"""
"""
__author__ = 'Alisue <lambdalisue@hashnote.net>'
import json
from utils.path import get_user_config_path


class Settings(object):
    # A dictionary to connect parser class and shortcut name
    parsers = {
        'shell': 'displayboard.parsers.shell.ShellParser',
        'markdown': 'displayboard.parsers.markdown.MarkdownParser',
        'plaintext': 'displayboard.parsers.plaintext.PlainTextParser',
    }

    # Default parser used if user does not specified parser
    default_parser = 'markdown'

    # Qt4 backend specification. The followings are available
    #   'PySide' - Use PySide
    #   'PyQt'   - Use PyQt4
    # If the specified backend is not available, it automatically use another
    backend = 'PySide'

    def get_filename(self):
        """
        Return a full path of the configuration file
        """
        filename = get_user_config_path('displayboard.js')
        return filename

    def save(self, filename=None):
        """
        Save configuration to the specified file.
        It no filename is specified, filename returned from get_filename
        method is used.
        """
        filename = filename or self.get_filename()
        data = {k: v for k, v in self.__dict__.iteritems()
                if not k.startswith('__')}
        with open(filename, 'wb') as fo:
            json.dump(data, fo, sort_keys=True, indent=4)

    def load(self, filename=None):
        """
        Load configuration from the specified file.
        It no filename is specified, filename returned from get_filename
        method is used.
        """
        filename = filename or self.get_filename()
        with open(filename, 'rb') as fi:
            data = json.load(fi)
            [setattr(self, k, v) for k, v in data.iteritems()]
        return self

# global instance
settings = Settings()
settings.load()
