#19/03/2020
# n = int(input())
# s = set()
# for i in range(n):
#     ele =map(int,input().split())
#     s.add(ele)
# li = []
# for i in s:
#     li.append(i)
# print(li[-2])

count = int(input())
n = map(int,input().split())
s = set()
li =[]
for i in n:
    s.add(i)
for i in s:
    li.append(i)
li.sort()
print(li[-2])
