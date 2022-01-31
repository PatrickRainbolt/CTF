# PicoCTF GYM: 
![Screenshot from 2022-01-31 15-47-24](https://user-images.githubusercontent.com/38919321/151870580-79db87bf-d124-4b42-a192-2074d0afe70c.png)



• [Addadshashanammu.zip](https://mercury.picoctf.net/static/3afd18a65e42b80526aa87f9766c588b/Addadshashanammu.zip)

# Downloading File:
Using "wget" on Linux to download the file. 
```
> wget "https://mercury.picoctf.net/static/3afd18a65e42b80526aa87f9766c588b/Addadshashanammu.zip"
Addadshashanammu.zip     100%[==================================================================>]   4.4K      

```

# UnZipped the file:
After using wget to download the Archive file I am using Unzip to extract the files. 
```
> unzip Addadshashanammu.zip 

Archive:  Addadshashanammu.zip
   creating: Addadshashanammu/
   creating: Addadshashanammu/Almurbalarammi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/
  inflating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet  

```

# Changing into the directory:
I used CD and tab completion to get to the correct directory.
```
> cd Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/

```

# What type of file:
I wanted to check they file type, to see where to go next.
```
> file fang-of-haynekhtnamet 
fang-of-haynekhtnamet: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=fcea24fb5379795a123bb860267d815e889a6d23, not stripped

```

# Checking Strings:
Using STRINGS and GREP to see if the flag is in clear text.
```
> strings fang-of-haynekhtnamet |grep picoCTF
*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_d32e018c}

```

# FLAG: 
```
picoCTF{l3v3l_up!_t4k3_4_r35t!_d32e018c}
```

