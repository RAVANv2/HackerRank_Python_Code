------------------- SET OPERATIONS ---------------------
1-> myset = set()
2-> myset.add('s') # This function add any value if value already exit than it does't pop error
3-> myset.update([1,3,4],(3,5)) # This function add all values to set irrespective with data type
4-> myset.discard(3) # Take single value as argument and removes single value from the set if value not exit than it do ot pop ant error
5-> myset.remove(4) # Take single argument and if value not exit than raise key error
6-> a.union(b) # Values which are exit both a or b 
7-> a.intersection(b) #Values which are exit both a and b
8-> a.difference(b) # Values which exit in a but not in b
9-> a.union(b) == b.union(a) # return True of False and same with intersection and difference
--------------------------------------------------------------