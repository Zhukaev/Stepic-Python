#1.2.11

ans = 0
newarr = []
for obj in objects:
	if (obj in newarr):
		ans = ans
	else:
		newarr.append(obj)
		ans = ans + 1
print(ans)