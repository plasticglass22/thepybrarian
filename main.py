import sys
import os
import glob
import re
import numpy
import utils
from collections import defaultdict

utils.spacer(1)

SEARCH_TERMS = sys.argv

if len(SEARCH_TERMS) > 1:
    print("Returning files related to: " + utils.colorstyle.LIGHTYELLOW + SEARCH_TERMS[1] + utils.colorstyle.GREEN)
    utils.osfullContents(".", SEARCH_TERMS[1])
else:
    print("Returning " + utils.colorstyle.LIGHTYELLOW + "everything" + utils.colorstyle.GREEN + " in this directory: ")
    utils.osfullContents(".", "")