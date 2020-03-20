#20/03/2020

# In this I approch to the solution in differnt way
# Making a list of list so that it is easy to store name and marks individually in the list


n = int(input())
li = []
for i in range(n):
    name, *line=input().split() 
    li.append([name, list(map(float, line))]) #For taking multiple values as input seperated by sppacebar than we take a pointer called as *line and put it down to list
ans = input()
for i in li:
    # print(i[1][0])
    if (ans==i[0]):
        avg = (i[1][0]+i[1][1]+i[1][2])/3
print("{:.2f}".format(avg))