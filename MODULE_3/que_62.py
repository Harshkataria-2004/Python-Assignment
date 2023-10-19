# Write a Python program to read a random line from a file. 

fp=open("abc.txt","w")
fp.write("hello my name is ishitajhduihduhdwddjiuuiuiw\nmkwohdiuwdhiwdhiudh\njhbduywuygduwj\n")
fp=open("abc.txt","r")
print(fp.readline())
fp.close()