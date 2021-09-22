#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    number = int(sys.argv[1])
    factors = []

    for whole_number in range(1, number + 1):
        if number % whole_number == 0:
            factors.append(-whole_number)
            factors.append(whole_number)

    print(factors)
else:
    print("SYNTAX ERROR: Invalid Arguments!   factor.py {value}")
