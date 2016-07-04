#3.4.6

import requests
import re

url1 = input()
urls = input()

patterna = r'<a[\w\W]+>[\w]<\/a>'
patternurl = r'https:\/\/[\w./]+\.html'
res = requests.get(url1)
temp = 0
allas1 = re.findall(patterna,res.text)
for a in allas1:
    allurls1 = re.findall(patternurl, res.text)
    for url2 in allurls1:
        res2 = requests.get(url2)
        allas2 = re.findall(patterna,res2.text)
        allurls2 = re.findall(patternurl, res2.text)
        if urls in allurls2:
            temp = 1
if temp == 1:
    print("Yes")
else:
    print("No")

#3.4.7

