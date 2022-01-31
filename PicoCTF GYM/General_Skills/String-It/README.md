# PicoCTF GYM: 
![Screenshot from 2022-01-31 17-38-12](https://user-images.githubusercontent.com/38919321/151884831-2be8af0f-afa7-4416-aa65-b094118a5f2f.png)

# Downloading File:
Using "wget" on Linux to download the file. 
```
> wget "https://jupiter.challenges.picoctf.org/static/5bd86036f013ac3b9c958499adf3e2e2/strings"
strings          100%[==================================================================>]   758K      

```

# File Type:
I checked to see what file type.
```
> file strings 
strings: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=047a5079a5f563cd0e540d28f42a37161093ffda, not stripped

```

# Using Strings:
I am using "strings" to pull out all text data and "grep" to look for a flag. This was a little confusing since the files was also called "strings".
```
> strings strings |grep "picoCTF"
picoCTF{5tRIng5_1T_827aee91}

```

# FLAG: strings it
```
picoCTF{5tRIng5_1T_827aee91}
```

