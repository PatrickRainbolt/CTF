# PicoCTF GYM: 
![Screenshot from 2022-01-31 17-07-53](https://user-images.githubusercontent.com/38919321/151881145-aa27c1ba-9288-4724-be7f-5f6d379aee92.png)

# Converting To ASCII:
It asked to conver hex 0x70 to ASCII code. I used "xxd" with "-r" tells it to convert hex to ascii as opposed to its normal mode 
of doing the opposite and"-p" tells it to use a plain format.
```
> echo "0x70" | xxd -r -p)
p

```

# Putting it all Together:
Now to put the "p" in a flag format.
```
> echo "picoCTF{$(echo "0x70" | xxd -r -p)}"
picoCTF{p}

```

# FLAG: Lets Warm Up
```
picoCTF{p}
```

