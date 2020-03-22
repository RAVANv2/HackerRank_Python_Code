#21/03/2020

# ---------------Approch-------------------
# First we check that the given string is lower or upper by islower() and isupper() function and then swap them by the help of lower() and upper() function

# ------------- What's new---------------
# 1-> islower() and isupper()  return true or False
# 2-> upper() and lower()   converts the string into lower and upper case

string = input()
newString = ""
for i in string:
    if (i.islower())==True:
        newString +=i.upper()
    elif (i.isupper())==True:
        newString +=i.lower()
    elif (i.isspace())==True:
        newString +=i
    else:
        newString+=i
print(newString)