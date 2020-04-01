
from itertools import permutations
li, n=input().split()
n=int(n)

print(*[''.join(i) for i in permutations(sorted(li),int(n))],sep='\n')
        


