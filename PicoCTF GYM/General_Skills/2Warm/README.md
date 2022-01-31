# PicoCTF GYM: 
![Screenshot from 2022-01-31 17-28-49](https://user-images.githubusercontent.com/38919321/151883748-7f1ee1e0-9f85-4f84-bdb2-dcc7e80dde2d.png)

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

