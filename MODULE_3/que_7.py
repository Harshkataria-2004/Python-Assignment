# Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given
# list of strings. 

a=["abc","aba","cbd","1221","eee"]
count=0
for i in a:
    if len(i)>2 and i[0]==i[-1]:
        count=count+1
print(count)