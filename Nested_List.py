#19/03/2020
if __name__ == "__main__":
    def Sort(li):
        l = len(li)
        for i in range(l):
            for j in range(l-i-1):
                if (li[j][1] > li[j+1][1]):
                    temp = li[j]
                    li[j] = li[j+1]
                    li[j+1] = temp
        for i in range(l):
            for j in range(l-i-1):
                if (li[j] > li[j+1]):
                    temp = li[j]
                    li[j] = li[j+1]
                    li[j+1] = temp
        return li[1][1],li



    count = int(input())
    mark = []
    for i in range(count):
        mark.append([input(),float(input())])
    ans,mark = Sort(mark)
    
    for i in mark:
        if i[1]==ans:
            print(i[0])
