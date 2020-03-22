#21/03/2020
def split_and_join(string):
    line = string.split(" ")
    line = "-".join(line)
    return line


string = input()
result = split_and_join(string)
print(result)