import re

def spacer(lines: int) -> None:
    """
    Adds a specified number of blank lines to CLI output as a spacer for formatting.

    :param: lines - integer value specifying number of blank lines to print
    """
    i = 1
    while i <= lines:
        print("")
        i += 1
