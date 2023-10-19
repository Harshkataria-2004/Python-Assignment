# Write a Python program to check multiple keys exists in a dictionary

a={
"name" : "ishita",
"roll_no" : 9,
"pass" : True
}
print(a.keys()>={"name","pass"})
print(a.keys()>={"name","9"})