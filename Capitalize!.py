#24/03/2020

#!/bin/python3
------------------------
1->word.capitalize() will capitalize the first letter of word 
------------------------


def solve(s):
    li = []
    for i in s:
        li.append(i.capitalize())
    return li

s = input().split(' ')
result = solve(s)
print(result)
