# PicoCTF GYM: 
![Mod-26](https://user-images.githubusercontent.com/38919321/134425073-4ff2f93e-ddec-426a-b0a4-e52c60cfce7c.png)


# Wrote a Python script to convert data into ROT13 format
```
> cat roth.py 
#!/usr/bin/env python

import codecs
import sys

if len(sys.argv) > 1:
    print(codecs.decode(sys.argv[1], 'rot_13'))
else:
    print "SYNTAX ERROR: Invalid Arguments!   roth.py {phrase}"
```

# Use script to convert data into ROT13 format
```
> ./roth.py "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_GYpXOHqX}"
picoCTF{next_time_I'll_try_2_rounds_of_rot13_TLcKBUdK}
```


# FLAG: Mod 26
```
picoCTF{next_time_I'll_try_2_rounds_of_rot13_TLcKBUdK}
```
