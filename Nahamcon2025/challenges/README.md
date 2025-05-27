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

![alt](cat.png)

I added the file type prefix, scaled the image using magick convert tool
```convert 957D.png -resize 200% flag.png```

and then extracted the text using tesseract
```tesseract 957D.png flag```

> `flag{Odb031ac265b3e6538aff0d9f456004f}`