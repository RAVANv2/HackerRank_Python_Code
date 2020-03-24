#24/03/2020

s1 = int(input())
set1 = set(map(int,input().split()))

s2 = int(input())
set2 = set(map(int, input().split()))

set1=set1.intersection(set2)
count=0
for i in set1:
    count+=1
print(count)