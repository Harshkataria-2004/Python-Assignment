# Write a Python program that will return true if the two given
# integervalues are equal or their sum or difference is 5.

num1 = int(input("Enter the 1st integer: "))
num2 = int(input("Enter the 2nd integer: "))
if num1 == num2 or num1 + num2 == 5 or abs(num1 - num2) == 5:
    result = True
else:
    result = False
print(result)
