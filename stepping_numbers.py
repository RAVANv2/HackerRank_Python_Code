
def is_stepping(x):
    s=str(x)
    if(len(s)==1):
        return 1
    else:
        for i in range(len(s)-1):
            p_digits=int(s[i])
            c_digits= int(s[i+1])
            if(abs(p_digits-c_digits)!=1):
                return 0
    return 1

t = int(input())
while(t):
    t-=1
    count=0
    n,m = map(int,input().split())
    for i in range(n,m+1):
        if(is_stepping(i)):
            count+=1
    print(count)
