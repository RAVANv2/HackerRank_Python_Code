#19/03/2020
def sortSecond(li):
    return li[1]

def sortFirst(li):
    return li[0]
mark = []
count = int(input())

for i in range(count):
    mark.append([input(), float(input())])
mark1 = mark
mark.sort(key = sortSecond)
mark1.sort(key = sortFirst)

ans = mark[1][1]
for i in mark1:
    if i[1]==ans:
        print(i[0])
