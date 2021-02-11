# Wordgen

## Dependencies:

Install `pypy3`. In short, `pypy3` is a faster `python3` interpreter.

## Why crunch sucks?

Wordgen is a python3 alternative to the yet popular
but slow and non-portable `crunch` wordlist generator.

Wordgen is much faster than crunch. Here is an example:

```
[luca@artix wordgen]$ time crunch 5 5  > /dev/null
Crunch will now generate the following amount of data: 71288256 bytes
67 MB
0 GB
0 TB
0 PB
Crunch will now generate the following number of lines: 11881376

real	0m3.632s
user	0m0.632s
sys	0m0.000s
[luca@artix wordgen]$ time ./wordgen.py 5 5  > /dev/null

real	0m1.959s
user	0m1.924s
sys	0m0.021s
[luca@artix wordgen]$
```

Almost two times faster. Also, `wordgen` is less
ressource-intensive than crunch.
I tried bruteforcing my own wifi with aircrack.
Aircrack is slow to start with crunch. It takes more
than 30 seconds to get 13,000 keys/s !!!!
Whereas with `wordgen` I instantly get 15,000 keys/s
as soon as I press enter.

Also, crunch is way too bloated. The man page of crunch
is 274 lines long!!!

## Usage

The usage is extremely easy. Just run
`./wordgen.py [min key length] [max key length] [alphabet: optionnal]`
if no alphabet is given, `wordgen` will pick the standart alphabet.
However here are some available alphabets:

| shortcut | description                          |
| :-       | :-:                                  |
| az       | normal alphabet in lower case letter |
| aZ       | lower case + upper case alphabet     |
| AZ       | upper case only                      |
| other    | input is the alphabet.               |

**Pro tip:** You can actually use an input file as
an alphabet. Run `xargs ./wordgen.py [your usual options] < alphabet.txt`.
