import re
import sys
import os
import glob
import numpy

## if these exist in a result string, don't print it.
EXCLUDE_PATTERNS = ["__pycache__"]

## strip these off of a result string for formatting and presentation
STRIP_PATTERNS = {
    "leading_dot" : "^."
}

def spacer(lines: int) -> None:
    """
    Adds a specified number of blank lines to CLI output as a spacer for formatting.

    :param: lines - integer value specifying number of blank lines to print
    """
    
    i = 1
    while i <= lines:
        print("")
        i += 1

def exclude() -> None:
    """
    Exclude certain items from the printed results. For use in contents() and fullContents().
    """

    

    raise NotImplementedError("exclude() is not implemented")

def fullContents(dir: str) -> None:
    """
    Recursively lists the contents of the specified directory, and it's subdirectories.

    :param: dir: str -> directory to begin recursive operation
    """

    glob_pattern = dir + "/**/*"
    rec_contents = glob.glob(glob_pattern, recursive=True)
    for item in rec_contents:
        print("item: ", str(item))

def contents(dir: str) -> None:
    """
    Lists the contents of just the directory specified as an argument.

    :param: dir: str -> the directory to print
    """

    glob_pattern = dir + "/*"
    dir_contents = glob.glob(glob_pattern)
    for item in dir_contents:
        print("item: ", str(item))