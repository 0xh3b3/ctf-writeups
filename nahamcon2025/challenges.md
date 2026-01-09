# $${\color{red}Free Flags!}$$


- **Category:** Warmups
- **Points:** 50
- **Solves:** 1150

---

## Challenge

> WOW!! Look at all these free flags!!
> But... wait a second... only one of them is right??
> **NOTE, bruteforcing flag submissions is still not permitted**. I will put a "max attempts" limit on this challenge at 1:00 PM Pacific to stop participants from automating submissions. There is only one correct flag, you can find a needle in a haystack if you really know what you are looking for.
> 
> **Attachment:** [free_flags.txt](https://ctf.nahamcon.com/files/cba72d2c0e710d0a5d692e0f53d6c049/free_flags.txt?token=eyJ1c2VyX2lkIjo1ODksInRlYW1faWQiOjE3NywiZmlsZV9pZCI6NDJ9.aDWN5g.I4O0uwoZUTilBWBcBqP5gbNR-Bc)
>
> ***Author:** John Hammond*

---

## Solution

After downloading the attachment I found out that it had a lot of flags :ok_woman:. On closer inspection though I noticed that almost all did not meet the full creteria of a flag format in accordance with the rules `flag\{[0-9a-f]{32}\}` they missed out on the inner condition `[0-9a-f]{32}`.

to find out the correct flag I came up with a python script to test the regex and return the flag with the correct format

```
import re

with open("free_flag.txt", "r") as f:
    file_handler = f.read()

match = re.search(r"flag\{[0-9a-f]{32}\}", file_handler)

if match:
    print(f"Match found: {match.group()}")
else:
    print("No match.")
```

and the flag was identified :trollface:

> Match found: `flag{ae6b6fb0686ec594652afe9eb6088167}`



# $${\color{red}The Martian}$$


- **Category:** Miscellaneous 
- **Points:** 50
- **Solves:** 647

---

## Challenge

> Wow, this file looks like it's from outta this world!
> 
> **Attachment:** [challenge.martian](https://ctf.nahamcon.com/files/b760e9f6a2e40670cb3aabd0c1d7c429/challenge.martian?token=eyJ1c2VyX2lkIjo1ODksInRlYW1faWQiOjE3NywiZmlsZV9pZCI6NDh9.aDWx7w.0_paKkP3-uSH8ziV_Dk_0bKlo2Y)
>
> ***Author:** John Hammond*

---

## Solution
The first step was enumeration and finding out what kind of file the eliens use, I ran file challenge.martian command and discovered that it was a data file

next I ran binwalk to extract hidden data
```binwalk -e challenge.martian```

Several files were extracted, I ran ```file *``` command to identify their file type, one file stood up in particular called `34` and `957D`, they were both images and they contained the flag 

![flag image](https://github.com/0xh3b3/ctf-writeups/blob/main/nahamcon2025/assets/34.png)

I added the file type prefix, scaled the image using magick convert tool
```convert 957D.png -resize 200% flag.png```

and then extracted the text using tesseract
```tesseract 957D.png flag```

> `flag{Odb031ac265b3e6538aff0d9f456004f}`



# $${\color{red}Read The Rules}$$


- **Category:** Miscellaneous 
- **Points:** 50
- **Solves:** 1369

---

## Challenge

> Please follow the rules for this CTF!
> 
> ***Author:** John Hammond*

---

## Solution
Basics 101 of CTFs always view page source 

I went to the page rules page and went through all the rules but the flag was not there, I viewed the page source and boom, I got the flag !!

> Read The Rules: ```flag{90bc54705794a62015369fd8e86e557b}```



# $${\color{red}Read The Rules}$$


- **Category:** Warmups
- **Points:** 50
- **Solves:** 1367

---

## Challenge

> Please follow the rules for this CTF!
> 
> ***Author:** John Hammond*

---

## Solution
Basics 101 of CTFs always view page source 

I went to the page rules page and went through all the rules but the flag was not there, I viewed the page source and boom, I got the flag !!

> Read The Rules: ```flag{90bc54705794a62015369fd8e86e557b}```



# $${\color{red}Technical Support}$$


- **Category:** Warmups 
- **Points:** 50
- **Solves:** 1069

---

## Challenge

> Want to join the party of GIFs, memes and emoji shenanigans? Or just want to ask a question for technical support regarding any challenges in the CTF?
> This CTF uses support tickets to help handle requests. If you need assistance, please create a ticket with the #ctf-open-ticket channel. You do not need to direct message any CTF organizers or facilitators, they will just tell you to open a ticket. You might find a flag in the ticket channel, though!

> Connect here: [Join ](https://ctf.nahamcon.com/discord)
> ***Author:** John Hammond*

---

## Solution

> This challenge was all about submitting a ticket for challenges a participant is facing

> The querry was flag and it returns the flag

> The bot is currently down ...



Thanks, xiexie


















