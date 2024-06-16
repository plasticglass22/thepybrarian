import sys
import utils
import aesth

aesth.spacer(1)

SEARCH_TERMS = sys.argv[1:]

if len(SEARCH_TERMS) == 1:
    print("Returning files related to: " + aesth.colorstyle.LIGHTYELLOW + SEARCH_TERMS[0] + aesth.colorstyle.GREEN)
    utils.fullContents(".", SEARCH_TERMS[0])
elif len(SEARCH_TERMS) == 2 and SEARCH_TERMS[0] == "-d":
    print("Returning contents of directory: " + aesth.colorstyle.LIGHTYELLOW + SEARCH_TERMS[1] + aesth.colorstyle.GREEN)
    utils.directorySearch(".", SEARCH_TERMS[1])
elif len(SEARCH_TERMS) == 0:
    print("Returning " + aesth.colorstyle.LIGHTYELLOW + "everything" + aesth.colorstyle.GREEN + " in this directory: ")
    utils.fullContents(".", "")
else:
    print("Error! Usage: python3 main.py [option] [search term]")