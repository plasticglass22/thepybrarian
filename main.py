import sys
import os
import glob
import re
import numpy
import utils
from collections import defaultdict

utils.spacer(1)

SEARCH_TERMS = sys.argv

if len(SEARCH_TERMS) > 2:
    print("Too many search terms. One at a time, please.")
elif len(SEARCH_TERMS) > 1:
    print("Returning items related to: ", SEARCH_TERMS[1])
    utils.osfullContents(".", SEARCH_TERMS[1])
else:
    print("Returning everything in this directory: ")
    utils.osfullContents(".", "")