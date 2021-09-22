# PicoCTF 2021: 
![Wave-a-flag](https://user-images.githubusercontent.com/38919321/134432565-2edcf4b8-03e9-4cc2-831a-aed14301087e.png)





# Downloading File:
Using "wget" on Linux to download the file. 
```
> wget "https://mercury.picoctf.net/static/a00f554b16385d9970dae424f66ee1ab/warm"
warm		100%[==================================================================>]  10.68K
```


# Examine File:
Using "file" in Linux to determine what type of file I downloaded. It appears to be a "ELF 64-bit LSB" files.
```
> file warm 
warm: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=985d9586d46e8651ab66c2fbb5a5473492466aa3, with debug_info, not stripped
```


# Setting Executable:
Using "chmod" on Linux to set the file to be exicutable. If this was not from a CTF site I would not suggest doing this except in a sandbox system.
```
> chmod +x warm 
```


# Executing the File:
After running the file I recieved a message telling me to use "-h" argument. When I executed it with the "-h" argument I recieved the flag.
```
> ./warm 
Hello user! Pass me a -h to learn what I can do!

> ./warm -h
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_18788aaa}
```


# FLAG: Wave a flag
```
picoCTF{b1scu1ts_4nd_gr4vy_18788aaa}
```
