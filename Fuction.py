#19/03/2020
def is_leap(year):
    leap = False
    if year%4==0 and year%100!=0:
        leap=True
    elif year%400==0:
        leap=True
    return leap

year = int(input())
bool=is_leap(year)
print(bool)
