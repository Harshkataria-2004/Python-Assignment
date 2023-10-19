# Write a Python script to concatenate following dictionaries to create a
# new one. 

dict1={1:2,2:3}
dict2={3:4,4:5}
dict3={}
for i in (dict1,dict2):
    dict3.update(i)
print(dict3)