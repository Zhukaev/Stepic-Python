#3.2.6

s = input()
a = input()
b = input()
count = 0;
if a not in s:
    print("0")
elif a in b and a in s:
    print("Impossible")
else:
    while a in s:
        s = s.replace(a, b)
        count = count + 1
    print(count)
	
#3.2.7

s = input()
t = input()
count = 0
while t in s:
    s = s[s.find(t) + 1:len(s)]
    count = count + 1

print(count)