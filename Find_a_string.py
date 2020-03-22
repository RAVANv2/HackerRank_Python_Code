
string = input()
sub = input()
k=0
count=0
flag=0
for i in range(len(string)):
    k=i
    for j in range(len(sub)):
        if (string[k]==sub[j]):
            k=k+1
            count=count+1
    if count==len(sub):
        flag = flag+1
print(flag)