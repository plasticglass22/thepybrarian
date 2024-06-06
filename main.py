import sys
import os
import glob
import re
import numpy

## get name of CWD

cwd_name = os.getcwd()
print("current location: ", cwd_name)

## get names of objects (files and/or subdirs) in CWD
cwd_contents = glob.glob('./**/*.*', recursive=True)
for item in cwd_contents:
    print("item: ", str(item))