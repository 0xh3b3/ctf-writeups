# Bunny go3s brr

- **Category:** Crypto
- **Points:** 150
- **Level:** Easy

---

## challenge
> This encryption goes brrr. A fast, furious encryption scheme was used to protect something important, and now all you see is nonsense. 
> This bunny doesn’t hide eggs it hides flags.

> **Author:** mburk4

![Bunny_go3s_brrr](src/Bunny_go3s_brrr.txt)

---

## Solution

- We are provided with a file containing gibberish that closely ressembles base 64 but on decoding from base64 it still gives some gibberish.
- A quick google using hints from the title and challenge instructions. The word `bunny` can be interpreted as rabbit, search for rabbit encryption and we get several decoders which confirms it as a valid encryption type,
- This website was used to decode, [Rabbit Encryption Enc|Dec](https://www.browserling.com/tools/rabbit-decrypt)

```
A hare may look small and cute, but it is very clever and quick. When danger comes, it does not fight—it thinks fast and runs in tricky ways so no one can catch it easily. Rabbits are good at hiding, changing direction, and confusing anyone who tries to follow them. That is how encryption works too: it hides a message so only someone smart can understand it. Just like a clever rabbit turning and hopping to stay safe, a message can be mixed up and protected until the right person comes along. If you follow the bunny carefully and think step by step, you might find the secret it is hiding:
cyberCC{7h1s_cunn1n9_sh0uld_63_h4r3_3ncrypt10n}
```

## Flag
> **Flag:** cyberCC{7h1s_cunn1n9_sh0uld_63_h4r3_3ncrypt10n}