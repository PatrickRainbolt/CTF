# PicoCTF GYM: 
![Screenshot from 2022-02-04 15-37-07](https://user-images.githubusercontent.com/38919321/152600003-b1445fab-bc47-4527-afad-3f2ce84ded3f.png)

# Netcat Away:
I had to use 'nc' or Netcat to remotely connect to server "jupiter.challenges.picoctf.org" on port "29221". It asked to convert data to continue:
- First set of numbers was Binary to ASCII string.
- Second set of numbers was Octal to ASCII string.
- Third set of numbers was Hexidecimal to ASCII string. 
```
> nc jupiter.challenges.picoctf.org 29221
Let us see how data is stored
you have 45 seconds.....

Please give the 01101100 01101001 01111010 01100001 01110010 01100100 as a word.
 Input: lizard

Please give me the  160 151 145 as a word.
 Input: pie

Please give me the 6c696d65 as a word.
 Input: lime

You've beaten the challenge
Flag: picoCTF{learning_about_converting_values_00a975ff}
```

# FLAG: Based
```
picoCTF{learning_about_converting_values_00a975ff}
```

