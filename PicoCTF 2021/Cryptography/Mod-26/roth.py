#!/usr/bin/env python

import codecs
import sys

if len(sys.argv) > 1:
    print(codecs.decode(sys.argv[1], 'rot_13'))
else:
    print "SYNTAX ERROR: Invalid Arguments!   roth.py {phrase}"
