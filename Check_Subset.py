#28/03/2020

t = int(input())
for i in range(t):
    n = int(input())
    setA = set(map(int, input().split()))
    n = int(input())
    setB = set(map(int, input().split()))
    if(setA.issubset(setB)):
        print(True)
    else:
        print(False)