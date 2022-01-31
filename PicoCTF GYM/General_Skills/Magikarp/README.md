# PicoCTF GYM: 


# Server:
I started the server from the CTF page. 


# Using Webshell to SSH to server:
Using "wget" on Linux to download the file. 
```
> ssh ctf-player@venus.picoctf.net -p 49746
ctf-player@venus.picoctf.net's password: 
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 5.4.0-1041-aws x86_64)

```


# Getting Part 1:
I logged in and got the first part of the flag.
```
> ctf-player@pico-chall$ pwd
/home/ctf-player/drop-in

> ctf-player@pico-chall$ ls -l
total 8
-rw-r--r-- 1 ctf-player ctf-player 14 Mar 16  2021 1of3.flag.txt
-rw-r--r-- 1 ctf-player ctf-player 56 Mar 16  2021 instructions-to-2of3.txt

> ctf-player@pico-chall$ cat 1of3.flag.txt 
picoCTF{xxsh_

```


# Getting Part 2:
Reading the instruction file I found the location of part 2.
```
> ctf-player@pico-chall$ cat drop-in/instructions-to-2of3.txt 
Next, go to the root of all things, more succinctly `/`

> ctf-player@pico-chall$ cd /

> ctf-player@pico-chall$ cat 2of3.flag.txt 
0ut_0f_\/\/4t3r_
```

# Getting Part 3:
Reading the instruction file I found the location of part 3.
```
ctf-player@pico-chall$ cat /instructions-to-3of3.txt 
Lastly, ctf-player, go home... more succinctly `~`

> ctf-player@pico-chall$ cd /home/ctf-player/

> ctf-player@pico-chall$ cat 3of3.flag.txt 
21cac893}

```

# Putting it all Together:
Using a view commands I first used "cat" to view the contines of the files, then piped it through "tr" to remove the newlines, and the put a echo at the end.
```
> cat /home/ctf-player/drop-in/1of3.flag.txt /2of3.flag.txt /home/ctf-player/3of3.flag.txt | tr -d '\n'; echo
picoCTF{xxsh_0ut_0f_\/\/4t3r_21cac893}

```


# FLAG: Magikarp Ground Mission
```
picoCTF{xxsh_0ut_0f_\/\/4t3r_21cac893}
```

