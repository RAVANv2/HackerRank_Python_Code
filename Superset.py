#28/03/2020

Set = set(map(int, input().split()))
n = int(input())
ans = []
for i in range(n):
    setA = set(map(int, input().split()))
    if(Set.issuperset(setA)):
        ans.append(1)
    else:
        ans.append(0)
if (0 in ans):
    print(False)
else:
    print(True)