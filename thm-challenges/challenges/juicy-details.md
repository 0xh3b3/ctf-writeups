# [Juicy Details](https://tryhackme.com/room/juicydetails)
***
## Introduction
---
You were hired as a SOC Analyst for one of the biggest Juice Shops in the world and an attacker has made their way into your network. 

Your tasks are:

1. Figure out what techniques and tools the attacker used
2. What endpoints were vulnerable
3. What sensitive data was accessed and stolen from the environment

An IT team has sent you a zip file containing logs from the server. Download the attached file, type in "I am ready!" and get to work! There's no time to lose!
***
## Reconnaissance
---
### task:
What tools did the attacker use? (Order by the occurrence in the log)
### solution:
+ For this Task we put in consideration that most hacking tools can be known by looking at the User-Agent Header
+ The User agent Header is is a characteristic string that lets servers and network peers identify the application, operating system, vendor, and/or version of the requesting
+ Severs use this to identify bots and tools
+ The user agent is part of the content that is captured by logs

N/B: Most tools have options to mask the real User-Agent as a way to evade detection i.e *--random-agent in sqlmap*

```
cat access.log
```

>__nmap, hydra, sqlmap, curl, feroxbuster__
***
### task
What endpoint was vulnerable to a brute-force attack?What endpoint was vulnerable to a brute-force attack?

### solution
+ Now that we have identified the tools used in this attack from the previous task, we can limit those tools to their function to solve this task
+ we are aware that hydra is a brute force tools, we will limit our search to hydra user agent as manually looking at all the logs is a waste of time and you may miss something important
+ I grepped out hydra with ignore case flag because I was not sure of the case used
```
cat access.log | grep -i "hydra"
```

>/rest/user/login

***
### task
What endpoint was vulnerable to SQL injection?
### solution
+ Similar to the previous task, I identified the tool used and in this case it was sqlmap, a popular sql injection exploitation tools
```
cat access.log | grep -i sqlmap
```

>/rest/products/search
***
### task
What parameter was used for the SQL injection?
### solution
This stask is similar to the previous task
>q
***
### task
What endpoint did the attacker try to use to retrieve files? (Include the /)
### solution
+ while following along the endpoints I came across a certain endpoint with parameters with file extentions being requested from the server. The edpoint had a familiar name ftp, which made me to relate it to the famous file transfer protocol

>/ftp
***
## Stolen Data
---
## task
What section of the website did the attacker use to scrape user email addresses?
## solution

>product reviews
---
## task
Was their brute-force attack successful? If so, what is the timestamp of the successful login? (Yay/Nay, 11/Apr/2021:09:xx:xx +0000)
## solution
>Yay, 11/Apr/2021:09:16:31 +0000
---
## task
What user information was the attacker able to retrieve from the endpoint vulnerable to SQL injection?
## solution
>email, password
---
## task
What files did they try to download from the vulnerable endpoint? (endpoint from the previous task, question #5)
## solution
>coupons_2013.md.bak, www-data.bak
---
## task
What service and account name were used to retrieve files from the previous question? (service, username)
## solution
>ftp, anonymous
---
## task
What service and username were used to gain shell access to the server? (service, username)
## solution
>ssh, www-data
---


