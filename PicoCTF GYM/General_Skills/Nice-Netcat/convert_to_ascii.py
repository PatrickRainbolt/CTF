#!/usr/bin/env python

import sys
import base64

text_out = ""
text_file = open(sys.argv[1], "r")
lines = text_file.readlines()

for line in lines:
    text_out = text_out + chr(int(line))
text_file.close()
print (text_out)
