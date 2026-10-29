
# [OLD SESSIONS](https://learn.cylabacademy.org/library/739?page=1&category=1&difficulty=1)

**author:** "David Gaviria"\
**date:** 2026-10-30\
**tags:** [web, easy, picoCTF2026]\

## Description
Proper session timeout controls are critical for securing user accounts. If a user logs in on a public or shared computer but doesn’t explicitly log out (instead simply closing the browser tab), and session expiration dates are misconfigured, the session may remain active indefinitely.\
This then allows an attacker using the same browser later to access the user’s account without needing credentials, exploiting the fact that sessions never expire and remain authenticated.

## Solution

When we follow the challenge link we are met with a default login page. 

![App Screenshot](https://dummyimage.com/468x300?text=App+Screenshot+Here)

Lets try creating an account and log in using dummy/test credentials Username: `test` Password:`test`

We use the dummy credentials and log in as the `test` user

![App Screenshot](https://dummyimage.com/468x300?text=App+Screenshot+Here)

![App Screenshot](https://dummyimage.com/468x300?text=App+Screenshot+Here)

On the `test` user we see a user hinting about the existense of a sensitive `sessions` directory, the directory leaks `sensitive information`; session tokens

One session token belongs to the `admin` user which contains the hidden `flag`

![App Screenshot](https://dummyimage.com/468x300?text=App+Screenshot+Here)

![App Screenshot](https://dummyimage.com/468x300?text=App+Screenshot+Here)

![App Screenshot](https://dummyimage.com/468x300?text=App+Screenshot+Here)

**Flag:** `academy{s3t_s3ss10n_3xp1rat10n5_3a931aa0}`

## Scripts

### Python
[old-sessions.py](https://dummyimage.com/468x300?text=App+Screenshot+Here)

