#22/03/2020


# N, M = input().split()
# N = int(N)
# M = int(M)
# c=".|."

# for i in range(N//2):
#     print(("-").ljust((N+2)-(i*3),"-")+c*(i*2+1)+"-".rjust((N+2)-(i*3),"-"))
# print("WELCOME".center(N*3,"-"))
# for i in range(N//2-1,-1,-1):
#     print(("-").ljust((N+2)-(i*3),"-")+c*(i*2+1)+"-".rjust((N+2)-(i*3),"-"))

n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
new = pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]
print(new)
print('\n'.join(new))


------------------------------------------------------------
concat the pattern list with "\n"
After Concatination "WELCOME" than concat pattern in reverse order
------------------------------------------------------------