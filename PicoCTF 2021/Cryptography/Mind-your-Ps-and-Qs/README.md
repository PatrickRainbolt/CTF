# PicoCTF 2021: 
![Mind-your-Ps-and-Qs](https://user-images.githubusercontent.com/38919321/134411085-5336edc8-4d4b-42cf-8b7b-4af4b8514b92.png)


# Get Value file using WGET in Linux:
```
> wget https://mercury.picoctf.net/static/38f30029ab93478310e906d3d084a4c1/values<br>
values         100%[===============================================================================>] 205KB/s

> cat values 
Decrypt my super sick RSA:
c: 240986837130071017759137533082982207147971245672412893755780400885108149004760496
n: 831416828080417866340504968188990032810316193533653516022175784399720141076262857
e: 65537
```


# Now break the "n" value into its factors.
Open [factordb.com](http://factordb.com) and paste the value of "n" into the Fatorize field and then press the "Factorize!" button. When the factors appear you can right click each factor and open in a new tab. Then the value in the Factorize window you can copy and paste.

```
left_value: 1593021310640923782355996681284584012117
right_value: 521911930824021492581321351826927897005221
```


# Create a program to decrypt the RSA key message

```
> cat rsa.py
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
```


# Modify the "c", "n", "e", "Left_value" and "right_value" variable and run script.
```
> ./rsa.py 
[13016382529449106065927291425342535437996222135352905256639592405461024281868413]
[b'picoCTF{sma11_N_n0_g0od_23540368}']
```


# FLAG: Mind your Ps and Qs
```
picoCTF{sma11_N_n0_g0od_23540368}
```

