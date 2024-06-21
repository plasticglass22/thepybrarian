#!/usr/bin/env python3

import sys
import utils
import aesth
import npyscreen as nps
import tui

# aesth.spacer(1)

# if __name__ == '__main__':
#     # pb = tui.Pybrarian().run()
#     results = nps.wrapper_basic(tui.search)
#     utils.printResults(results[1], results[0], False)
#     aesth.spacer(1)
#     print("Thank you for using Pybrarian!")

aesth.spacer(1)

SEARCH_TERMS = sys.argv[1:]

if len(SEARCH_TERMS) == 1:
    print("Returning files related to: " + aesth.colorstyle.LIGHTYELLOW + SEARCH_TERMS[0] + aesth.colorstyle.GREEN)
    utils.fullContents(".", SEARCH_TERMS[0], False)
elif len(SEARCH_TERMS) == 2 and SEARCH_TERMS[0] == "-d":
    print("Returning contents of directory: " + aesth.colorstyle.LIGHTYELLOW + SEARCH_TERMS[1] + aesth.colorstyle.GREEN)
    utils.fullContents(".", SEARCH_TERMS[1], True)
elif len(SEARCH_TERMS) == 0:
    print("Returning " + aesth.colorstyle.LIGHTYELLOW + "everything" + aesth.colorstyle.GREEN + " in this directory: ")
    utils.fullContents(".", "", False)
else:
    print(aesth.colorstyle.ERROR + "Error!" + aesth.colorstyle.GREEN + " Usage: python3 main.py [option] [search term]")