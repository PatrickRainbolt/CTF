# PicoCTF GYM: 
![Screenshot from 2022-01-31 17-19-42](https://user-images.githubusercontent.com/38919321/151882639-dcf4636b-28c5-43a3-9e32-93faca1fd8e9.png)

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

