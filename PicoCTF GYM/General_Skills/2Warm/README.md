# PicoCTF GYM: 




# Converting To Decimal:
It asked to conver 43 in Decimal to Binary or Base 2. I used linux "echo" with "bc" to do the convertion.
```
> echo "obase=2;42" | bc
101010

```

# Putting it all Together:
Now to put the "p" in a flag format.
```
> echo "picoCTF{$(echo "obase=2;42" | bc)}"
picoCTF{101010}

```

# FLAG: 2Warm
```
picoCTF{101010}
```

