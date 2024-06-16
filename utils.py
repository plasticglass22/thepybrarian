import re
import sys
import os
import glob
import numpy
from collections import defaultdict

## if these exist in a result string, don't print it.
EXCLUDE_PATTERNS = ["__pycache__", "git", ".vscode"]

class colorstyle:
    RED = '\033[91m'
    DIRHEADER = '\033[1m\033[94m\033[4m'
    NORMAL = '\033[0m'
    GREEN = '\033[92m'
    LIGHTCYAN = '\033[96m'
    LIGHTYELLOW = '\033[93m'

def spacer(lines: int) -> None:
    """
    Adds a specified number of blank lines to CLI output as a spacer for formatting.

    :param: lines - integer value specifying number of blank lines to print
    """
    
    i = 1
    while i <= lines:
        print("")
        i += 1

def osfullContents(dir: str, searchterm: str) -> None:
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

    ITER_ITEMS = list(sorted(CONTENTS.items()))

    if searchterm != "":
        for i in range(0, len(ITER_ITEMS)):
            levels = ITER_ITEMS[i][0].count("/")
            for j in range(0, len(ITER_ITEMS[i][1])):
                if searchterm in ITER_ITEMS[i][1][j]:
                    print("")
                    print(colorstyle.DIRHEADER + ITER_ITEMS[i][0] + colorstyle.NORMAL)
                    print("")
                    print(colorstyle.GREEN + " \u2517" + levels*"\u2501\u2501 " + ITER_ITEMS[i][1][j])
                else:
                    pass
    else:
        for i in range(0, len(ITER_ITEMS)):
            levels = ITER_ITEMS[i][0].count("/")
            print("")
            print(colorstyle.DIRHEADER + ITER_ITEMS[i][0] + colorstyle.NORMAL) ## PRINTING DIRECTORY NAME
            print("")
            for j in range(0, len(ITER_ITEMS[i][1])):
                print(colorstyle.GREEN + " \u2517" + levels*"\u2501\u2501 " + ITER_ITEMS[i][1][j]) ## PRINTING FILENAME

    spacer(1)