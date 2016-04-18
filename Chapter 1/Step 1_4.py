#1.4.8
def getNameSpace(myVar, nameSpace):
    if myVar in namespaces[nameSpace]["vars"]:
        print(nameSpace)
    elif namespaces[nameSpace]["parent"] != None:
        nameSpace = namespaces[nameSpace]["parent"]
        getNameSpace(myVar, nameSpace)
    else:
        print(None)

namespaces = {"global": {"parent": None, "vars": []}}
n = int(input())
for i in range(n):
    comand = input().split()
    if comand[0] == "create":
        namespaces[comand[1]] = {"parent": comand[2], "vars": []}
    elif comand[0] == "add":
        namespaces[comand[1]]["vars"].append(comand[2])
    elif comand[0] == "get":
        nameSpace = comand[1]
        myVar = comand[2]
        getNameSpace(myVar, nameSpace)
