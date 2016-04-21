#2.2.5

import datetime
a = input().split()
year = int(a[0])
month = int(a[1])
day = int(a[2])
delta = int(input())

a = datetime.date(year, month, day)
b = datetime.timedelta(days=delta)
c = a + b
str = str(c.year) + " " + str(c.month) + " " + str(c.day)
print(str)

#2.2.9

import simplecrypt
passwords = ["9XB8nsIqRfYeswC","4sEhUGLEZti9BiN","bDjmT0NcIW8nzhb","ZN6QQoMOO1ZQLUY","RVrF2qdMpoq6Lib","tnnX7HH3vJ9Hiji","C24TJYYkqekv40l","B2ropluPaMAitzE","DRezNUVnr2zC0CP","XCNmpTvvZb1n3mX"]
with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
for password in passwords:
    try:
        print(simplecrypt.decrypt(password,encrypted))
    except simplecrypt.DecryptionException:
        print("not a password")