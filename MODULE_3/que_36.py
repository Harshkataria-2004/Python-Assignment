# Write a Python script to check if a given key already exists in a
# dictionary. 

n={'1':2,'7':3,'8':4,'5':7,'9':0,'8':5}
a=input("enter:")
if a in n.keys():
    print("key is present")
else:
    print("key is not present")