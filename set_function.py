#19/03/2020
n = int(input())
s=[]
for i in range(1,n+1):
    s.append(i)
opt = int(input())
for i in range(0,opt):
    opt_name = input()
    if opt_name=="pop":
        s.pop()
    elif opt_name=="remove":
        x = int(input())
        s.remove(x)
    elif opt_name=="discard":
        x = int(input())
        s.discard(x)
print(sum(s))
