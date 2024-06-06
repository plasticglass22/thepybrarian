import sys
import os
import glob
import re
import numpy
import utils

## get name of CWD

cwd_name = os.getcwd()
print("current location: ", cwd_name)

utils.spacer(1)

## get names of objects (files and/or subdirs) in CWD
## simple get and print for a first step
## DELETE THIS BLOCK: MADE REDUNDANT BY UTILS.FULLCONTENTS()
# cwd_contents_rec = glob.glob('./**/*', recursive=True)
# for item in cwd_contents_rec:
#     print("item: ", str(item))

## mess around with the new fullContents() func

# utils.fullContents(cwd_name)
## this givess too much info, because os.getcwd() gets FULL path

utils.fullContents(".")
## this is the way to go i think, doesn't expose dir names above cwd

utils.spacer(2)

utils.contents(".")