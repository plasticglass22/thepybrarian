import re
import sys
import os
import glob
import numpy
from collections import defaultdict

## if these exist in a result string, don't print it.
EXCLUDE_PATTERNS = ["__pycache__", "git", ".vscode"]

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

def osfullContents(dir: str) -> None:
    """
    Recursively lists the contents of the specified directory and its subdirectories.

    This method uses os.walk()

    :param: dir: str -> the directory to begin recursive operations.
    """

    ## THIS GETS THE RIGHT OUTPUT
    ## JUST NEEDS TO BE FORMATTED

    directories = []
    formatteddirs = []
    filenames = []

    CONTENTS = defaultdict(list[str])

    cwd = "/" + os.getcwd()[os.getcwd().rfind("/"):]

    for root, subdirs, files in os.walk(dir, topdown=True):
        for file in files:
            #######################################
            # DIRNAMES
            for item in EXCLUDE_PATTERNS:
                if item not in root:
                    directories.append(root)
                    pass
                else:
                    root = ""
            for dir in directories:
                for item in EXCLUDE_PATTERNS:
                    if item not in dir:
                        pass
                    else:
                        dir = ""
            fdir = cwd[1:] + dir[1:]
            if dir != "": formatteddirs.append(fdir)
            ########################################
            # FILENAMES
            ########################################
            path = str("/" + file)
            for item in EXCLUDE_PATTERNS:
                if item not in path:
                    pass
                else:
                    path = ""
            if path != "" and root != "": 
                filenames.append(path)
            #########################################
            if dir != "": CONTENTS[fdir].append(path[1:])

    dirname0 = list(sorted(CONTENTS.items()))[0]
    fnames0 = list(sorted(CONTENTS.items()))[0][1]

    spacer(1)

    ITER_ITEMS = list(sorted(CONTENTS.items()))

    for i in range(0, len(ITER_ITEMS)):
        print(ITER_ITEMS[i][0])
        for j in range(0, len(ITER_ITEMS[i][1])):
            print("\u2517\u2501\u2501 " + ITER_ITEMS[i][1][j])

    spacer(1)