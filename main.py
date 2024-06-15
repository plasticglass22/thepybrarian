import sys
import os
import glob
import re
import numpy
import utils
from collections import defaultdict

# utils.spacer(2)

# print("glob contents()")
# utils.Gcontents(".")

# utils.spacer(2)

# print("os.walk fullContents()")
utils.osfullContents(".")

test_contents = list(os.walk(".", topdown=True))

def files(filepath, filetype):
    paths = []