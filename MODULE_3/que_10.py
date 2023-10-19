# Write a Python function that takes two lists and returns true if they have
# at least one common member. 

a=[1,2,4,7,"tushar","fruit",8,9]
b=[3,5,6,4,0,66]
result=False
for i in a:
    for j in b:
        if i==j:
            result = True
print(result)