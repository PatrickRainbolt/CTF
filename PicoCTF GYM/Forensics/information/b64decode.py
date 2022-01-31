#!/usr/bin/env python

import sys
import base64

decoded = base64.b64decode(sys.argv[1])
print "Decoded: [" + decoded + "]"
