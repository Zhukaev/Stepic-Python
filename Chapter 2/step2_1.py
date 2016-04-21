#2.1.5

try:
    foo()
except ZeroDivisionError:
    print("ZeroDivisionError ")
except ArithmeticError:
    print("ArithmeticError")
except AssertionError:
    print("AssertionError")

#2.1.6

def isParentEx(nameErr, flag):
    if errors[nameErr]["exept"] == True:
        return True
    else:
        for parentName in errors[nameErr]["parent"]:
            flag = isParentEx(parentName, flag)
    return flag

errors = {"name": {"parent": [], "exept": False}}
n = int(input())
for i in range(n):
    names = input().split()
    errName = names.pop(0)
    errors[errName] = {"parent":[], "exept": False}
    for name in names:
        if name != ":":
            errors[errName]["parent"].append(name)

m = int(input())
for i in range(m):
    nameErr = input()
    a = isParentEx(nameErr, False)
    if a == True:
        print(nameErr)
    errors[nameErr]["exept"] = True
	
#2.1.8

class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x <= 0:
            raise NonPositiveError
        else:
            list.append(self, x)