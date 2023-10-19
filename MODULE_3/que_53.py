# Write a Python function that checks whether a passed string is palindrome
# or not 

def palindrome(i):
    if i==i[::-1]:
        print("it is")
    else:
        print("is not")
i=input("enter somthing:")
print(palindrome(i))