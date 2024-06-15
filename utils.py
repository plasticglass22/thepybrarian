import re
import sys
import os
import glob
import numpy

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

def exclude() -> None:
    """
    Exclude certain items from the printed results. For use in contents() and fullContents().
    """

    

    raise NotImplementedError("exclude() is not implemented")

def GfullContents(dir: str) -> None:
    """
    Recursively lists the contents of the specified directory, and it's subdirectories.

    This method uses glob.glob()

    :param: dir: str -> directory to begin recursive operation
    """

    glob_pattern = dir + "/**/*"
    rec_contents = glob.glob(glob_pattern, recursive=True)
    for item in rec_contents:
        print("item: ", str(item))

def Gcontents(dir: str) -> None:
    """
    Lists the contents of just the directory specified as an argument.

    This method uses glob.glob()

    :param: dir: str -> the directory to print
    """

    glob_pattern = dir + "/*"
    dir_contents = glob.glob(glob_pattern)
    for item in dir_contents:
        print("item: ", str(item))

def osfullContents(dir: str) -> None:
    """
    Recursively lists the contents of the specified directory and its subdirectories.

    This method uses os.walk()

    :param: dir: str -> the directory to begin recursive operations.
    """

    ## THIS GETS THE RIGHT OUTPUT
    ## JUST NEEDS TO BE FORMATTED

    directories = []

    cwd = "/" + os.getcwd()[os.getcwd().rfind("/"):]

    spacer(1)

    for root, subdirs, files in os.walk(dir, topdown=True):
        for file in files:
            # print(root + os.sep + file)
            for item in EXCLUDE_PATTERNS:
                if item not in root:
                    directories.append(root)
                    pass
                else:
                    root = ""
            # if root != "": print(root)
            for dir in directories:
                for item in EXCLUDE_PATTERNS:
                    if item not in dir:
                        pass
                    else:
                        dir = ""
            if dir != "": print(cwd[1:] + dir[1:])
            path = str("/" + file)
            for item in EXCLUDE_PATTERNS:
                if item not in path:
                    pass
                else:
                    path = ""
            if path != "" and root != "": 
                # print(root)
                print("\u2517\u2501\u2501" + path[1:])

    spacer(1)