#22/03/2020
import textwrap as tw

------------------------------------
1-> textwrap class have a function wrap function which returns list
it will wrap the string into given width 

2-> string.join(iterable) it return a string with concatination of two strings
------------------------------------
s = input()
w = int(input())

# li = tw.wrap(s,w)
# for i in li:
#     print(i)

def wrap(s,w):
    li=[]
    for i in range(0,len(s),w):
        li = s[i:i+w]
    "\n".join(li)
    return li

YOu also write the wrap function in this way:
def wrap(s,w):
    return "\n".join([s[i:i+w] for i in range(0,len(s),w)])

result =wrap(s,w)
print(result)