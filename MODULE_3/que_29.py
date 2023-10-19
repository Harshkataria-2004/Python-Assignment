# Write a Python program to find the repeated items of a tuple. 

set1=set()
a=(12,45,67,90,32,54,65,90,67,32)
for i in a:
    if a.count(i)>1:
        set1.add(i)
print(set1)