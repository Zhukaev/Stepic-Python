#1.6.7

def isAParent(parent, child, flag):
    if parent == child:
        return 1
    elif parent in classes[child]["parent"]:
        return 1
    else:
        for parentName in classes[child]["parent"]:
            flag = isAParent(parent, parentName, flag)
    return flag

classes = {"name": {"parent": []}}
n = int(input())
for i in range(n):
    names = input().split()
    className = names.pop(0)
    classes[className] = {"parent":[]}
    for name in names:
        if name != ":":
            classes[className]["parent"].append(name)

m = int(input())
for i in range(m):
    names = input().split()
    parent = names[0]
    child = names[1]
    a = isAParent(parent, child, 0)
    if a == 0:
        print("No")
    else:
        print("Yes")

#1.6.8

class ExtendedStack(list):
    def sum(self):
        a = self.pop()
        b = self.pop()
        self.append(a + b)
# операция сложения

    def sub(self):
        a = self.pop()
        b = self.pop()
        self.append(a - b)
# операция вычитания

    def mul(self):
        a = self.pop()
        b = self.pop()
        self.append(a * b)
        
# операция умножения

    def div(self):
        a = self.pop()
        b = self.pop()
        self.append(a // b)
		
#1.6.9

class LoggableList (list, Loggable):
    def append(self, a):
        self.log(a)