import re
import sys
import os
from collections import defaultdict

class colorstyle:
    """
    Class of color/formatting values for STDOUT output.
    """
    RED = '\033[91m'
    GREEN = '\033[0m\033[92m'
    LIGHTCYAN = '\033[96m'
    LIGHTYELLOW = '\033[93m'
    DIRHEADER = '\033[1m\033[94m\033[4m'
    NORMAL = '\033[0m'
    ERROR = '\033[91m\033[1m\033[4m'

def spacer(lines: int) -> None:
    """
    Adds a specified number of blank lines to STDOUT output for formatting.

    :param: lines: int -> number of blank lines to print.
    """
    
    i = 1
    while i <= lines:
        print("")
        i += 1