import requests
import re
url = input()
pattern = r'<img.*? src="(.+?)".*?>'
res = requests.get(url)
#print(res.text)
#print(res)
allimgs = re.findall(pattern, res.text)
good = 0
for img in allimgs:
#    print(requests.get(img).headers.get('Content-Type'))
    if requests.get(img).status_code == 200 and 'image' in requests.get(img).headers.get('Content-Type'):
        good += 1
print(good)
#https://stepic.org/media/attachments/lesson/25669/sample.html
# <img alt='src="https://sdlksldk"' src="dklskd">
