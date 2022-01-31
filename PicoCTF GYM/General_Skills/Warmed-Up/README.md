# PicoCTF GYM: 




# Converting To Decimal:
It asked to conver Hex "0x3D" to base 10 or Decimal. I used linux "echo" with base 16 or "16#".
```
> echo $((16#3D))
61

```

# Putting it all Together:
Now to put the "p" in a flag format.
```
> echo "picoCTF{$(echo $((16#3D)))}"
picoCTF{61}

```

# FLAG: Warmed Up
```
picoCTF{61}
```

