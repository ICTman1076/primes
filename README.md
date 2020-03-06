# ICTman1076/primes

**A list of nearly 3 MILLION primes**, with more added by an automated program every
24 hours, hosted on [PythonAnywhere](https://pythonanywhere.com). Thanks to them
for not banning me yet ;)

The most up-to-date version is on
(https://ictman1076.eu.pythonanywhere.com/optimusPrime.txt) but I provided a
mirror here just to make it easier to find.

**As for the repo, it's originally hosted on [GitLab](https://gitlab.com/ICTman1076/primes)** -
this is the only one that ICTman will attempt to keep up to date. I may provide
mirrors to other services that are linked to the GitLab repo and I will do my
best to ensure the two repos match, but I cannot guarantee it.

**Do not use in mission-critical situations.** I am not guaranteeing that all of
these are truly prime numbers - I may have made a mistake in the code (although,
I don't think I have) and may be generating utter nonsense, so don't rely on this.
**I expressly disallow use of these prime numbers for public-facing cryptography**
(but personal projects, and other projects not involving cryptography, are ok,
just follow the APL-1.0 licence in the repo).

## WARNING about the difference between this one and the PythonAnywhere one
The Git repo uses new lines (`\n`) to seperate primes, however, the
PythonAnywhere list is formatted in JSON. The reason is because JSON makes life
easier when using the list, whereas using new lines for each prime means within
Git it is easier to see what new prime numbers have been generated when. Some
older commits before [bcabc886](https://gitlab.com/ICTman1076/primes/-/commit/bcabc8866284a9e9a9a867ce887ae199d8a60f5e)
still used JSON, as well, so beware of that.

## LICENSE

It's Open Source! I mean, there's not a lot of source to open, but whatever.
It's currently under APL-1.0, check the license file.