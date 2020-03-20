#20/03/2020

# What's New !!!
# insert(index,element)   if you insert two element on same index than it increase previous same index element index by 1 
# remove(element)  It shows error if element is not present 

n = int(input())
li = []

for i in range(n):
    cmd, *line= input().split()
    integer = list(map(int,line))
    if cmd=="insert":
        li.insert(integer[0],integer[1])
    elif cmd=="remove":
        li.remove(integer[0])
    elif cmd=="print":
        print(li)
    elif cmd=="append":
        li.append(integer[0])
    elif cmd=="sort":
        li.sort()
    elif cmd=="pop":
        li.pop()
    elif cmd=="reverse":
        li.reverse()