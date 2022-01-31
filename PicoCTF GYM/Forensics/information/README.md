# PicoCTF GYM: 
![information](https://user-images.githubusercontent.com/38919321/134426194-a8ae603c-2121-4279-8f06-1dec79afeb2a.png)


# Photo of a cat
[cat.jpg](https://mercury.picoctf.net/static/7cf6a33f90deeeac5c73407a1bdc99b6/cat.jpg)


# WGET File
Using "wget" in Linux to download the "cat.jpg" file
```
> wget "https://mercury.picoctf.net/static/7cf6a33f90deeeac5c73407a1bdc99b6/cat.jpg"
cat.jpg		100%[==================================================================>] 857.55K    
```


# Eye of GNOME
Using this to view the "cat.jpg" file in Linux. Nothing in the image was useful
```
> eog cat.jpg &
```


# Strings
Using Linux "strings" to search for useful ASCII data but found nothing useful
```
> strings cat.jpg | grep pico
```


# Install ExifToo 
Decided to install ExifTool, a platform-independent Perl library plus a command-line application for reading, writing and editing meta information in a wide variety of files. 

```
> sudo apt install exiftool
```

# Using "Exiftool" to view Metadata of the file.
```
> exiftool cat.jpg 
ExifTool Version Number         : 11.16
File Name                       : cat.jpg
Directory                       : .
File Size                       : 858 kB
File Modification Date/Time     : 2021:03:15 14:24:46-04:00
File Access Date/Time           : 2021:08:27 16:51:44-04:00
File Inode Change Date/Time     : 2021:08:27 16:50:02-04:00
File Permissions                : rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
Copyright Notice                : PicoCTF
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                          : PicoCTF
Image Width                     : 2560
Image Height                    : 1598
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2560x1598
Megapixels                      : 4.1
```

# Found data
I think the data is stored in one of these two Meta data fields but they failed submission.
```
Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
```

# Base64 Decode
I also noticed the data was in a Base64 format. So I wrote a Base64 Decoder in Python to test my theory.
```
> cat b64decode.py 
#!/usr/bin/env python

import sys
import base64
decoded = base64.b64decode(sys.argv[1])
print "Decoded: [" + decoded + "]"
```

# Found Results
I tested the two fields with my decoder and got the following results.
```
> ./b64decode.py "7a78f3d9cfb1ce42ab5a3aa30573d617"
Decoded: [���w}q��q�6i�Zݦ�Ӟ�w�{]
> ./b64decode.py "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9"
Decoded: [picoCTF{the_m3tadata_1s_modified}]
```


# FLAG: Information
```
picoCTF{the_m3tadata_1s_modified}
```
