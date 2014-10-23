# coding=utf-8
"""
"""
__author__ = 'Alisue <lambdalisue@hashnote.net>'
import os
import platform


def get_user_config_path(filename, appname=None):
    """
    Get user config filename.

    It will return operating system dependent config filename.

    Parameters
    ----------
    filename : string
        A filename
    appname : string or None
        An application name used in path. It is automatically guessed from
        filename if it is not specified.

    Returns
    -------
    string
        A full path of user configuration file

    """
    if appname is None:
        appname = os.path.splitext(os.path.basename(filename))[0]
    system = platform.system()
    if system == 'Windows':
        rootname = os.path.join(os.environ['APPDATA'], appname)
        prefix = ''
    elif system == 'Linux':
        XDG_CONFIG_HOME = os.environ.get('XDG_CONFIG_HOME', None)
        rootname = XDG_CONFIG_HOME or os.path.join('~', '.config')
        rootname = os.path.expanduser(rootname)
        # check if XDG_CONFIG_HOME exists
        if not os.path.exists(rootname) and XDG_CONFIG_HOME is None:
            # XDG_CONFIG_HOME is not used
            rootname = os.path.expanduser('~')
            prefix = '.'
        else:
            rootname = os.path.join(rootname, appname)
            prefix = ''
    elif system == 'Darwin':
        rootname = os.path.expanduser('~')
        prefix = '.'
    else:
        # Unknown
        rootname = os.path.expanduser('~')
        prefix = ''
    return os.path.join(rootname, prefix + filename)
