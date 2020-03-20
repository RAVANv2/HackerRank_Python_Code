#20/03/2020

# What's New!!!
# hash(object) That function generates a hash code which was unique
# You did't add element in tuple so you need to form new tuble every time while adding element with + 

t = ()
n = int(input())
li = list(map(int,input().split()))

for i in range(n):
    ele = li[i]
    t = t+(ele,)
print(hash(t))