#!/usr/bin/env python3

from Crypto.Util.number import inverse
from Crypto.Util.number import long_to_bytes

c = 240986837130071017759137533082982207147971245672412893755780400885108149004760496
n = 831416828080417866340504968188990032810316193533653516022175784399720141076262857
e = 65537

left_value = 1593021310640923782355996681284584012117
right_value = 521911930824021492581321351826927897005221

# Compute the Totiemt Function
totient = (left_value - 1) * (right_value - 1)

# Compute the Modular Multiplicative Inverse - This is the private key.
d = inverse(e, totient)

# If "c" was the irigianl text an you wanted to encode it use pow(m, e, n)
m = pow(c, d, n)    # Computes original message by "c" raised to "d" mod "n"

print("[" + str(m) + "]")
print("[" + str(long_to_bytes(m)) + "]")
