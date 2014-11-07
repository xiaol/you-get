#!/usr/bin/env python

import os, sys

_is_ansi_terminal = os.getenv('TERM') in (
    'eterm-color',
    'linux',
    'screen',
    'vt100',
    'xterm',
)

# ANSI escape code
# See <http://en.wikipedia.org/wiki/ANSI_escape_code>
RESET = 0
BOLD = 1
UNDERLINE = 4
NEGATIVE = 7
NO_BOLD = 21
NO_UNDERLINE = 24
POSITIVE = 27
BLACK = 30
RED = 31
GREEN = 32
YELLOW = 33
BLUE = 34
MAGENTA = 35
CYAN = 36
LIGHT_GRAY = 37
DEFAULT = 39
BLACK_BACKGROUND = 40
RED_BACKGROUND = 41
GREEN_BACKGROUND = 42
YELLOW_BACKGROUND = 43
BLUE_BACKGROUND = 44
MAGENTA_BACKGROUND = 45
CYAN_BACKGROUND = 46
LIGHT_GRAY_BACKGROUND = 47
DEFAULT_BACKGROUND = 49
DARK_GRAY = 90                 # xterm
LIGHT_RED = 91                 # xterm
LIGHT_GREEN = 92               # xterm
LIGHT_YELLOW = 93              # xterm
LIGHT_BLUE = 94                # xterm
LIGHT_MAGENTA = 95             # xterm
LIGHT_CYAN = 96                # xterm
WHITE = 97                     # xterm
DARK_GRAY_BACKGROUND = 100     # xterm
LIGHT_RED_BACKGROUND = 101     # xterm
LIGHT_GREEN_BACKGROUND = 102   # xterm
LIGHT_YELLOW_BACKGROUND = 103  # xterm
LIGHT_BLUE_BACKGROUND = 104    # xterm
LIGHT_MAGENTA_BACKGROUND = 105 # xterm
LIGHT_CYAN_BACKGROUND = 106    # xterm
WHITE_BACKGROUND = 107         # xterm

def sprint(text, *colors):
    """Format text with color or other effects into ANSI escaped string."""
    return "\33[{}m{content}\33[{}m".format(";".join([str(color) for color in colors]), RESET, content=text) if _is_ansi_terminal and colors else text

def write_log(tag, text, *colors):
    """Print a log message to standard error."""
    sys.stderr.write(sprint("{}\t{}".format(tag, text), *colors) + "\n")

def log(tag, message, details='', exit_code=None, *colors):
    """"""
    text = '{}\n\t\t{}'.format(message, details) if details else message
    write_log(tag, text, *colors)
    if exit_code is not None:
        exit(exit_code)

def i(message, details='', exit_code=None):
    """Print a normal log message."""
    log('[    LOG]', message, details, exit_code)

def d(message, details='', exit_code=None):
    """Print a debug log message."""
    log('[  DEBUG]', message, details, exit_code, BLUE)

def w(message, details='', exit_code=None):
    """Print a warning log message."""
    log('[WARNING]', message, details, exit_code, YELLOW)

def e(message, details='', exit_code=None):
    """Print an error log message."""
    log('[  ERROR]', message, details, exit_code, YELLOW, BOLD)

def wtf(message, details='', exit_code=1):
    """What a Terrible Failure!"""
    log('[  FATAL]', message, details, exit_code, RED, BOLD)
