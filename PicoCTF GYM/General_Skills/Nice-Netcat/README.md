# PicoCTF 2021: 
![Nice-netcat](https://user-images.githubusercontent.com/38919321/134429037-a6404c1a-69f4-4820-975c-bed25c18531f.png)


# What is Netcat
Netcat (often abbreviated to nc) is a computer networking utility for reading from and writing to network connections using TCP or UDP. The command is designed to be a dependable back-end that can be used directly or easily driven by other programs and scripts. At the same time, it is a feature-rich network debugging and investigation tool, since it can produce almost any kind of connection its user could need and has a number of built-in capabilities.


# Netcat File
Using Netcat and capturing the output to to a file. Had to hit CTRL C to save file. Output.txt file was all numbers between 0 and 255.
```
> nc mercury.picoctf.net 22902 > output.txt
```


# Checking for ASCII
Using Linux "head" command to view the first 7 value, coverting the value from decimal to ASCII. 
```
> head -7 output.txt 
112 
105 
99 
111 
67 
84 
70 
```


# ASCII Table
This output converts to picoCTF in ASCII.
![ASCII-Table](https://user-images.githubusercontent.com/38919321/134429918-521bc652-aaf9-4855-87e5-9828c19e8fb8.png)



# Converting Decimal to ASCII
I wrote a Python script to convert the decimal numbers output in the file to ASCII and display the output.
```
> cat convert_to_ascii.py 
#!/usr/bin/env python

import sys
import base64

text_out = ""
text_file = open(sys.argv[1], "r")
lines = text_file.readlines()

for line in lines:
    text_out = text_out + chr(int(line))
text_file.close()
print (text_out)
```


# Executing Script
```
> ./convert_to_ascii.py output.txt 
picoCTF{g00d_k1tty!_n1c3_k1tty!_d3dfd6df}
```


# FLAG: Nice Netcat
```
picoCTF{g00d_k1tty!_n1c3_k1tty!_d3dfd6df}
```

