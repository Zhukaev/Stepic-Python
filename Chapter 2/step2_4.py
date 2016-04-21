#2.4.4

f = open("dataset_24465_4.txt","r")
fileData = f.read()
print(fileData)
arrayData = fileData.split()
print(arrayData)
a = len(arrayData) - 1
f.close()
f = open("test.txt","w")
for i in range(len(arrayData)):
    f.write(arrayData[a])
    f.write('\n')
    a = a - 1
f.close()

#2.4.6

import os

for current_dir, dirs, files in os.walk("main"):
    dirs = []
    #print (current_dir, files)
    for file in files:
        if ".py" in file:
            if current_dir in dirs:
                pass
            else:
                dirs.append(current_dir)
    for dir in dirs:
        print(dir)