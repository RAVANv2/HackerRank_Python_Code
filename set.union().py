#24/03/2020

s1 = int(input())
set1 = set(map(int,input().split()))

s2 = int(input())
set2 = set(map(int, input().split()))

print(set1.union(set2))