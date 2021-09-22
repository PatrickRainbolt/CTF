# PicoCTF 2021: 
![Transformation](https://user-images.githubusercontent.com/38919321/134433481-7dc1b922-254b-4f82-b82b-9957f9a2b85b.png)


# Encoded File:
[enc](https://mercury.picoctf.net/static/0d3145dafdc4fbcf01891912eb6c0968/enc)


# Downloading File:
Using "wget" on Linux to download the "enc" file.
```
> wget "https://mercury.picoctf.net/static/0d3145dafdc4fbcf01891912eb6c0968/enc"
enc		100%[==================================================================>]      57K
```


# Inspecting File:
Using "file" on Linux to determine what type of file we downloaded. It appears to be a "UTF-8 Uicode" file.
```
> file enc 
enc: UTF-8 Unicode text, with no line terminators
```


# Viewing Encoded File:
Using "cat" on Linux to view the contents of the "enc" file.
```
>cat enc 
灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ
```


# CyberChef: 
I as not sure how this was really encoded, so I opened up [CyberChef](https://gchq.github.io/CyberChef/), then pasted "enc" data into the input, dragged magic into the Recipe field and looked through the Output section.
![CyberChef](https://user-images.githubusercontent.com/38919321/134433992-493c1b23-d278-4d04-85f1-5d0e9e2ab312.png)



# Next Step:
I scanned through the output and found "Encoded_text('UTF-16BE(1201)')".
```
Recipe:					Result snippet:					Properties:
Encode_text('UTF-16BE (1201)')		picoCTF{16_bits_inst34d_of_8_26684c20}		Valid UTF8 Entropy: 4.32
```


 FLAG: Transformation
```
picoCTF{16_bits_inst34d_of_8_26684c20}
```

