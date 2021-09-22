#!/usr/bin/env python

import codecs
import sys

if len(sys.argv) > 1:
    # phrase = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_GYpXOHqX}"

    print(codecs.decode(sys.argv[1], 'rot_13'))
else:
    print "SYNTAX ERROR: Invalid Arguments!   roth.py {phrase}"
