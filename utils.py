import re
import sys
import os
from collections import defaultdict
import aesth
import npyscreen as nps

## if these exist in a result string, don't print it.
EXCLUDE_PATTERNS = ["__pycache__", "git", ".vscode"]

# def fullContents(dir: str, searchterm: str, diropt: bool) -> None:
def fullContents(dir: str, searchterm: str, diropt: bool) -> list[tuple[str, list[str]]]:
    """
    Recursively lists the contents of the specified directory and its subdirectories.

    This function automatically passes the query results to printResults().

    :param: dir: str -> the directory to begin recursive operations.
    :param: searchterm: str -> search term supplied as CLI argument.
    :param: diropt: bool -> if True, searches by directory name.
    """

    ## lists for result processing
    directories = []
    formatteddirs = []
    filenames = []

    ## container for results of walk
    CONTENTS = defaultdict(list[str])

    ## trim off part of path above starting directory
    cwd = "/" + os.getcwd()[os.getcwd().rfind("/"):]

    ## recursively walk through directories, add items to lists initialized above
    for root, subdirs, files in os.walk(dir, topdown=True):
        for file in files:
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
            # FILENAMES
            path = str("/" + file)
            for item in EXCLUDE_PATTERNS:
                if item not in path:
                    pass
                else:
                    path = ""
            if path != "" and root != "": 
                filenames.append(path)
            if dir != "": CONTENTS[fdir].append(path[1:])

    ## remove duplicates from results, put them in order
    ## 'sorted' puts the dirs in alphabetical order. lets subdirs be grouped together 
    ## because they have the same parent dir.
    ITER_ITEMS = list(sorted(CONTENTS.items()))

    # return ITER_ITEMS

    if diropt == False:
        printResults(ITER_ITEMS, searchterm, False)
    elif diropt == True:
        printResults(ITER_ITEMS, searchterm, True)

def printResults(contents: list[tuple[str, list[str]]], searchterm: str, diropt: bool) -> None:
    """
    Prints the results of the query to STDOUT.

    This functionality was initially part of fullContents(), but was moved out for portability.

    :param: contents: list[tuple[str, list[str]]] -> full contents of directory and sub directories.
    :param: searchterm: str -> search term supplied as CLI argument.
    :param: diropt: bool -> if True, searches by directory name.
    """
    if diropt != True:
        if searchterm != "":
            for i in range(0, len(contents)):
                levels = contents[i][0].count("/")
                fnames = []
                dnames = []             
                for j in range(0, len(contents[i][1])):
                    if searchterm.lower() in contents[i][1][j].lower():
                        dnames.append(contents[i][0])
                        fnames.append(contents[i][1][j])
                    else:
                        pass
                dnames = list(set(dnames))
                for dname in dnames:
                    print("")
                    print(aesth.colorstyle.DIRHEADER + dname + aesth.colorstyle.NORMAL)
                    print("")
                    for fname in fnames:
                        print(aesth.colorstyle.GREEN + " \u2517" + levels*"\u2501\u2501 " + fname)
            fnames.clear()
            dnames.clear()
        else:
            for i in range(0, len(contents)):
                levels = contents[i][0].count("/")
                print("")
                print(aesth.colorstyle.DIRHEADER + contents[i][0] + aesth.colorstyle.NORMAL) ## PRINTING DIRECTORY NAME
                print("")
                for j in range(0, len(contents[i][1])):
                    print(aesth.colorstyle.GREEN + " \u2517" + levels*"\u2501\u2501 " + contents[i][1][j]) ## PRINTING FILENAME
    elif diropt == True:
        if searchterm != "":
            for i in range(0, len(contents)):
                levels = contents[i][0].count("/")
                if searchterm.lower() in contents[i][0].lower():
                    print("")
                    print(aesth.colorstyle.DIRHEADER + contents[i][0] + aesth.colorstyle.NORMAL)
                    print("")
                for j in range(0, len(contents[i][1])):
                    if searchterm.lower() in contents[i][0].lower():
                        print(aesth.colorstyle.GREEN + " \u2517" + levels*"\u2501\u2501 " + contents[i][1][j])
                    else:
                        pass
        else:
            for i in range(0, len(contents)):
                levels = contents[i][0].count("/")
                print("")
                print(aesth.colorstyle.DIRHEADER + contents[i][0] + aesth.colorstyle.NORMAL) ## PRINTING DIRECTORY NAME
                print("")
                for j in range(0, len(contents[i][1])):
                    print(aesth.colorstyle.GREEN + " \u2517" + levels*"\u2501\u2501 " + contents[i][1][j]) ## PRINTING FILENAME

    aesth.spacer(1)


def printResultsForm(contents: list[tuple[str, list[str]]], searchterm: str, diropt: bool) -> None:
    """
    Prints the results of the query to STDOUT.

    This functionality was initially part of fullContents(), but was moved out for portability.

    :param: contents: list[tuple[str, list[str]]] -> full contents of directory and sub directories.
    :param: searchterm: str -> search term supplied as CLI argument.
    :param: diropt: bool -> if True, searches by directory name.
    """
    if diropt != True:
        if searchterm != "":
            for i in range(0, len(contents)):
                levels = contents[i][0].count("/")
                fnames = []
                dnames = []             
                for j in range(0, len(contents[i][1])):
                    if searchterm.lower() in contents[i][1][j].lower():
                        dnames.append(contents[i][0])
                        fnames.append(contents[i][1][j])
                    else:
                        pass
                dnames = list(set(dnames))
                for dname in dnames:
                    print("")
                    print(aesth.colorstyle.DIRHEADER + dname + aesth.colorstyle.NORMAL)
                    print("")
                    for fname in fnames:
                        print(aesth.colorstyle.GREEN + " \u2517" + levels*"\u2501\u2501 " + fname)
            fnames.clear()
            dnames.clear()
        else:
            for i in range(0, len(contents)):
                levels = contents[i][0].count("/")
                print("")
                print(aesth.colorstyle.DIRHEADER + contents[i][0] + aesth.colorstyle.NORMAL) ## PRINTING DIRECTORY NAME
                print("")
                for j in range(0, len(contents[i][1])):
                    print(aesth.colorstyle.GREEN + " \u2517" + levels*"\u2501\u2501 " + contents[i][1][j]) ## PRINTING FILENAME
    elif diropt == True:
        if searchterm != "":
            for i in range(0, len(contents)):
                levels = contents[i][0].count("/")
                if searchterm.lower() in contents[i][0].lower():
                    print("")
                    print(aesth.colorstyle.DIRHEADER + contents[i][0] + aesth.colorstyle.NORMAL)
                    print("")
                for j in range(0, len(contents[i][1])):
                    if searchterm.lower() in contents[i][0].lower():
                        print(aesth.colorstyle.GREEN + " \u2517" + levels*"\u2501\u2501 " + contents[i][1][j])
                    else:
                        pass
        else:
            for i in range(0, len(contents)):
                levels = contents[i][0].count("/")
                print("")
                print(aesth.colorstyle.DIRHEADER + contents[i][0] + aesth.colorstyle.NORMAL) ## PRINTING DIRECTORY NAME
                print("")
                for j in range(0, len(contents[i][1])):
                    print(aesth.colorstyle.GREEN + " \u2517" + levels*"\u2501\u2501 " + contents[i][1][j]) ## PRINTING FILENAME

    aesth.spacer(1)