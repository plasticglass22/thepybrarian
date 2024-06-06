import sys
import os
import glob
import re
import numpy

## get name of CWD

cwd_name = os.getcwd()
print("current location: ", cwd_name)

## get names of objects (files and/or subdirs) in CWD
## simple get and print for a first step
cwd_contents_rec = glob.glob('./**/*', recursive=True)
for item in cwd_contents_rec:
    print("item: ", str(item))

## try to treat files and subdirs differently
## 