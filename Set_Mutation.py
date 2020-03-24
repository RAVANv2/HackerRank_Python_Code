#24/03/2020

n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    a,b = input().split()
    if a=='intersection_update':
        s1 = set(map(int, input().split()))
        s.intersection_update(s1)
    elif a=='update':
        li = list(map(int,input().split()))
        s.update(li)
    elif a=='symmetric_difference_update':
        s1 = set(map(int, input().split()))
        s.symmetric_difference_update(s1)
    elif a=='difference_update':
        s1 = set(map(int, input().split()))
        s.difference_update(s1)
print(sum(s))

