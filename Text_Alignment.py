#22/03/2020

---------------------- Approch--------------------------------
"String".ljust(width,"-") -> print string from left hand side to right hand side from range of index(width-len(string)) and print "-" in rest space
"String".rjust(width,"-") ->prints from right to left hand side
"string".center(width,"-") ->printing Start from center.
-----------------------------------------------------------------------

thickness = int(input())
c='H'

# Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1,"-") +c+ (c*i).ljust(thickness-1,"-"))

# Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2,"-")+(c*thickness).center(thickness*6,"-"))

# Belt line
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6,"-"))

# Lower Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2,"-")+(c*thickness).center(thickness*6,"-"))

# Lower Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness,"-")+c+(c*(thickness-i-1)).ljust(thickness,"-")).rjust(thickness*6,"-"))