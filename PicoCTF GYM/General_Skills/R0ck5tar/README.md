# PicoCTF GYM: 
![Screenshot from 2022-02-03 15-32-56](https://user-images.githubusercontent.com/38919321/152430917-0869b120-d5af-4d1a-b101-6a91a222d15c.png)


# Downloading File:
Using "wget" on Linux to download the file. 
```
> wget "https://jupiter.challenges.picoctf.org/static/b99c57e4274172bf3c93534b6d59632d/lyrics.txt"
lyrics.txt   		 100%[==================================================================>]   877K      

```

# Rockstar Lyrics:
Rockstar was created by Dylan Beattie whill drinking. He was tired of seeing "Are you a Rockstar Developer" on job postings. The language
is writing in 80's hair band lyrics. So first, lets look at the lyrics or program.
```
> cat lyrics.txt
Rocknroll is right              
Silence is wrong                
A guitar is a six-string        
Tommy's been down               
Music is a billboard-burning razzmatazz!
Listen to the music             
If the music is a guitar                  
Say "Keep on rocking!"                
Listen to the rhythm
If the rhythm without Music is nothing
Tommy is rockin guitar
Shout Tommy!                    
Music is amazing sensation 
Jamming is awesome presence
Scream Music!                   
Scream Jamming!                 
Tommy is playing rock           
Scream Tommy!       
They are dazzled audiences                  
Shout it!
Rock is electric heaven                     
Scream it!
Tommy is jukebox god            
Say it!                                     
Break it down
Shout "Bring on the rock!"
Else Whisper "That ain't it, Chief"                 
Break it down
```

# Rockstar Language layout:
Ther is a lot of information about the language at: "https://codewithrockstar.com/docs".


# Translating the Song Lyrics to Python Code:
Here is a side by side break down of the Song lyric to Python code.






# Running the Python code
I ran the code after saving it to "rockstar.py". 
- The first if ask: if the input is equal to 10. So you enter 10 and press Enter.
- The second if ask: if input minus 171 equal 0. So you enter 171 and press Enter.
- The following data is ASCII values that need to be converted to a string.

```
> python3 rockstar.py
10
Keep pn Rocking!
171
66
79
78
74
79
86
73
Bring on the rock!

```

# Converting ASCII to a String
There are many ways to do this so I created a quick command line entry.
```
echo "picoCTF{$(echo "66 79 78 74 79 86 73" | awk '{ for(i=1;i<=NF;i++) printf("%c",$i); print "";  }')}"
picoCTF{BONJOVI}

```



# FLAG: 1_wanna_b3_a_r0ck5tar
```
picoCTF{BONJOVI}
```

