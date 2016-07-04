#3.3.7

import sys
import re
pattern = r"cat"
for line in sys.stdin:
    line = line.rstrip()
    a = re.findall(pattern,line)
    if len(a) >= 2:
        print(line)

#3.3.8

import sys
import re
pattern = r'\bcat\b'
for line in sys.stdin:
    line = line.rstrip()
    a = re.findall(pattern,line)
    if len(a) != 0:
        print(line)

#3.3.9

import sys
import re
pattern = 'z\w\w\wz'
for line in sys.stdin:
    line = line.rstrip()
    a = re.findall(pattern,line)
    if len(a) != 0:
        print(line)

#3.3.10

import sys
import re
pattern = r'\\'
for line in sys.stdin:
    line = line.rstrip()
    a = re.findall(pattern,line)
    if len(a) != 0:
        print(line)

#3.3.11

import sys
import re
pattern = r'\b((\w+)\2)\b'
for line in sys.stdin:
    line = line.rstrip()
    a = re.findall(pattern, line)
    if len(a) != 0:
        print(line)

#3.3.12

import sys
import re
pattern = r'human'
for line in sys.stdin:
    line = line.rstrip()
    a = re.sub(pattern,"computer",line)
    print(a)

#3.3.13

import sys
import re
pattern = r'\b[aA]+\b'
for line in sys.stdin:
    line = line.rstrip()
    a = re.sub(pattern, 'argh', line, 1)
    print(a)

#3.3.14



#3.3.15

import sys
import re

pattern = r'(\w)(\1)+'
for line in sys.stdin:
    line = line.rstrip()
    a = re.sub(pattern, r'\1', line)
    print(a)  

#3.3.16

import sys
import re
pattern = r'\b[01]+\b'
for line in sys.stdin:
    line = line.rstrip()
    a = re.findall(pattern, line)
    if len(a) == 1:
        number = int(a[0],base=2)
        if number % 3 == 0:
            print(line)