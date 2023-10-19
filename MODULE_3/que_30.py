# Write a Python program to remove an empty tuple(s) from a list of tuples. 

a=[(),(),(34,65,87),("a","b","c")]
for i in a:
    if (len(i)==0):
        a.remove(i)
        print(a)