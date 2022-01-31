# PicoCTF GYM: 
![Screenshot from 2022-01-31 15-20-43](https://user-images.githubusercontent.com/38919321/151867123-ad044e4f-b3ff-4a1d-84e4-5c6383a4b102.png)

• [static](https://mercury.picoctf.net/static/ff4e569d6b49b92d090796d4631a2577/static)
• [BASH-script](https://mercury.picoctf.net/static/ff4e569d6b49b92d090796d4631a2577/ltdis.sh)


# Downloading File:
Using "wget" on Linux to download the file. 
```
> wget "https://mercury.picoctf.net/static/ff4e569d6b49b92d090796d4631a2577/static"
static          100%[==================================================================>]   8.2K      

> wget "https://mercury.picoctf.net/static/ff4e569d6b49b92d090796d4631a2577/ltdis.sh"
ltdis.sh        100%[==================================================================>]  785

```

# Looking at the BASH script:
The script does a objdump, to get the machine code, and a strings command, to get any ASCII data. These are both stored in seperate files.  
```
> head -25 static.ltdis.x86_64.txt 

static:     file format elf64-x86-64


Disassembly of section .text:

0000000000000530 <_start>:
 530:	31 ed                	xor    %ebp,%ebp
 532:	49 89 d1             	mov    %rdx,%r9
 535:	5e                   	pop    %rsi
 536:	48 89 e2             	mov    %rsp,%rdx
 539:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp
 53d:	50                   	push   %rax
 53e:	54                   	push   %rsp
 53f:	4c 8d 05 8a 01 00 00 	lea    0x18a(%rip),%r8        # 6d0 <__libc_csu_fini>
 546:	48 8d 0d 13 01 00 00 	lea    0x113(%rip),%rcx        # 660 <__libc_csu_init>
 54d:	48 8d 3d e6 00 00 00 	lea    0xe6(%rip),%rdi        # 63a <main>
 554:	ff 15 86 0a 20 00    	callq  *0x200a86(%rip)        # 200fe0 <__libc_start_main@GLIBC_2.2.5>
 55a:	f4                   	hlt    
 55b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000000560 <deregister_tm_clones>:
 560:	48 8d 3d d9 0a 20 00 	lea    0x200ad9(%rip),%rdi        # 201040 <__TMC_END__>
 567:	55                   	push   %rbp
 568:	48 8d 05 d1 0a 20 00 	lea    0x200ad1(%rip),%rax        # 201040 <__TMC_END__>


> head -25 static.ltdis.strings.txt 
    238 /lib64/ld-linux-x86-64.so.2
    290 >1FbY]
    361 libc.so.6
    36b puts
    370 __cxa_finalize
    37f __libc_start_main
    391 GLIBC_2.2.5
    39d _ITM_deregisterTMCloneTable
    3b9 __gmon_start__
    3c8 _ITM_registerTMCloneTable
    660 AWAVI
    667 AUATL
    6ba []A\A]A^A_
    6e8 Oh hai! Wait what? A flag? Yes, it's around here somewhere!
    7c7 ;*3$"
   1020 picoCTF{d15a5m_t34s3r_ccb2b43e}
   1040 GCC: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0
   1671 crtstuff.c
   167c deregister_tm_clones
   1691 __do_global_dtors_aux
   16a7 completed.7698
   16b6 __do_global_dtors_aux_fini_array_entry
   16dd frame_dummy
   16e9 __frame_dummy_init_array_entry
   1708 static.c
 
```


# Greping for the flag:
I used grep to search through both files and grab the flag. 
```
> grep picoCTF static.ltdis.*
static.ltdis.strings.txt:   1020 picoCTF{d15a5m_t34s3r_ccb2b43e}

```


# FLAG: Nice Netcat
```
picoCTF{d15a5m_t34s3r_ccb2b43e}
```

