# PicoCTF GYM: 
![Python-Wrangling](https://user-images.githubusercontent.com/38919321/134431444-5b4042b3-9049-4b0e-97c7-a6a456db093d.png)


# Files to Download:
[Python script](https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/ende.py)<br>
[password](https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/pw.txt)<br>
[flag](https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/flag.txt.en)<br>


# WGET Files
Using Linux "wget" to download the provided files.
```
> wget "https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/ende.py"
ende.py		100%[==================================================================>]     1.30K  

> wget "https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/pw.txt"
pw.txt		100%[==================================================================>]       33K

> wget "https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/flag.txt.en"
flag.txt.en	100%[==================================================================>]       140K
```


# Viewing the Password
Using Linux "cat" to view the content of the "pw.txt" file.
```
> cat pw.txt 
dbd1bea4dbd1bea4dbd1bea4dbd1bea4
```


# Understanding the Script
Reading through the "ende.py" code I determined that "-d" decodes the file using the password suplied in the "pw.txt" file.
```
> python3 ende.py -d flag.txt.en
Please enter the password:dbd1bea4dbd1bea4dbd1bea4dbd1bea4
picoCTF{4p0110_1n_7h3_h0us3_dbd1bea4}
```


# FLAG: Python Wrangling
```
picoCTF{4p0110_1n_7h3_h0us3_dbd1bea4}
```
