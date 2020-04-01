
lo = int(input())
for i in range(lo):
    n,m = input().split()
    n = int(n)
    m=int(m)

    count = int(n/m)
    li = []
    for i in range(1,count+1):
        ans = m*i
        ans = ans%10
        li.append(ans)
    print(sum(li))