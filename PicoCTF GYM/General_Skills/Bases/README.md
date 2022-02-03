# PicoCTF GYM: 


# Guessing this was Base64 Encoded:
From looking at the data, "bDNhcm5fdGgzX3IwcDM1', it looked Base64 encode. So I did a quick Command line convert.
```
> echo "bDNhcm5fdGgzX3IwcDM1" | base64 --decode ; echo
l3arn_th3_r0p35
```

# Converting to a Flag:
I changed my command line entry to create the flag output.
```
> echo "picoCTF{$(echo "bDNhcm5fdGgzX3IwcDM1" | base64 --decode ; echo)}"
picoCTF{l3arn_th3_r0p35}

```


# FLAG: what's a net cat
```
picoCTF{l3arn_th3_r0p35}

```
