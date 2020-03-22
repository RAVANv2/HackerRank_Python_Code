#21/03/2020 
string = input()
i, c = input().split()
i = int(i)
string = string[:i] +c+ string[i+1:]
print(string)