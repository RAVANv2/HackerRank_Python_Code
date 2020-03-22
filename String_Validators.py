#21/03/2020

s=input()
l = len(s) 
li=[]
for i in s:
    li.append(i)
for i in li:
    flag=0
    if i.isalnum()==True:
        print("True")
        flag=1
        break
if flag==0:
    print("False")
for i in li:
    flag=0
    if i.isalpha()==True:
        print("True")
        flag=1
        break
if flag==0:
    print("False")
for i in li:
    flag=0
    if i.isdigit()==True:
        print("True")
        flag=1
        break
if flag==0:
    print("False")

for i in li:
    flag=0
    if i.islower()==True:
        print("True")
        flag=1
        break
if flag==0:
    print("False")
for i in li:
    flag=0
    if i.isupper()==True:
        print("True")
        flag=1
        break
if flag==0:
    print("False")
