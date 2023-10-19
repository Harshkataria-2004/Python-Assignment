# Write a Python program to check whether a list contains a sub list 

a=[3,4,5,6,7,8,9]
b=[4,8,5]
c=0
result=False
for i in a:
    if i in b:
        c=c+1
    if(c==len(b)):
        result=True
print(result)