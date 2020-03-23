#23/03/2020

# Good Question
n = int(input())
for i in range(n):
    s = [chr(ord('a')+n-j-1) for j in range(i+1)]
    # print(s)
    s="-".join(s)
    # print((s+s[::-1][1:]).center(n*4-3, '-'))
    print((s+s[::-1][1:]).center(n*4-3, '-'))

for i in range(n-1):
    s = "-".join(chr(ord('a')+n-j-1) for j in range(n-i-1))
    print((s+s[::-1][1:]).center(n*4-3, '-'))

