#1.3.9

def closest_mod_5(x):
    if x % 5 == 0:
        return x
    else:
        x += 1
        return closest_mod_5(x)
		
#1.3.15

import itertools
n, k = map(int, input().split())

def C(n, k):
    return len(list(itertools.combinations(range(1, n + 1), k)))
    
print(C(n,k))