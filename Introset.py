#28/03/2020

n = int(input())
s = set(map(int, input().split()))
sum=0
length = len(s) 
for i in s:
    sum += i
print(sum/length)
print(s)