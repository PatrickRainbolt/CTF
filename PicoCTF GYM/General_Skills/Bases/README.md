# PicoCTF GYM: 
![Screenshot from 2022-02-03 16-32-25](https://user-images.githubusercontent.com/38919321/152434488-fbd3f01e-6d63-4783-a153-cfb1ae5f9cfd.png)


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


# FLAG: Bases
```
picoCTF{l3arn_th3_r0p35}

```
