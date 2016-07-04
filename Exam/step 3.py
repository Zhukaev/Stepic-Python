import sys
import re
pattern = r'\((.*?)\)'
for line in sys.stdin:
    line = line.rstrip()

    a = re.sub(pattern, '()', line)
    print(a)