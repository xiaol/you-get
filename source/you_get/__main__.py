#!/usr/bin/env python

import getopt, sys

from .utils.log import *
from .version import program_name, __version__

# Command-line options
_options = {
    'debug'     : ['d'],
    'force'     : ['f'],
    'gui'       : ['g'],
    'help'      : ['h'],
    'playlists' : ['l'],
    'version'   : ['V'],
}
_longopts = list(_options)
_shortopts = ''.join([opt for i in _options for opt in _options[i]])

# Help message
_help = """Usage: {} [OPTION]... [URL]...
TODO
""".format(program_name)

# Default configuration
_conf = {}

def get_help():
    """Get help message."""
    return _help

def get_conf(key):
    """Get configuration."""
    return _conf[key] if key in _conf else None

def set_conf(key, value):
    """Set configuration."""
    _conf[key] = value

def get_version():
    """Get semantic version number."""
    return __version__

def get_version_full(**kwargs):
    """Get current version."""
    import platform
    from .utils.git import get_head

    # Get (branch, commit) if running from a git repo.
    head = get_head(kwargs['repo_path'])

    return """{}:
    version:  {}
    branch:   {}
    commit:   {}
    platform: {}
    python:   {}""".format(sprint(program_name, BOLD),
        sprint(get_version(), BOLD),
        head[0] if head else '(stable)',
        head[1] if head else '(tag v{})'.format(get_version()),
        platform.platform(),
        sys.version.split('\n')[0])

def g(message, details='', exit_code=None):
    """Print a debug log message, if debugging is enabled."""
    if get_conf('debug'):
         d(message, details, exit_code)

def main(**kwargs):
    """Main entry point."""

    # Get options and arguments
    try:
        opts, args = getopt.getopt(sys.argv[1:], _shortopts, _longopts)
    except getopt.GetoptError as e:
        wtf('{}.'.format(e),
            "Try '{} --help' for more options.""".format(program_name))

    if not opts and not args:
        # Display help
        print(get_help())

    else:
        for opt, arg in opts:
            if opt in ('-h', '--help'):
                # Display help
                print(get_help())

            elif opt in ('-V', '--version'):
                # Display version
                print(get_version_full(**kwargs))

            elif opt in ('-d', '--debug'):
                # Enable debugging
                set_conf('debug', True)

            elif opt in ('-f', '--force'):
                # Force download
                set_conf('force', True)

            elif opt in ('-g', '--gui'):
                # Run using GUI
                set_conf('gui', True)

            elif opt in ('-l', '--playlist', '--playlists'):
                # Download playlist whenever possible
                set_conf('playlist', True)

        g(_longopts)
        g(_shortopts)

        if args:
            if get_conf('gui'):
                # Enter GUI mode
                from .gui import gui_main
                gui_main(*args, **conf)
            else:
                # Enter console mode
                from .console import console_main
                console_main(*args, **conf)



def main_legacy(**kwargs):
    from .common import main
    main()
