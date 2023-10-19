# Write a Python program to sum of three given integers. However, if two
# values are equal sum will be zero.

num1 = int(input("Enter the 1st integer: "))
num2 = int(input("Enter the 2nd integer: "))
num3 = int(input("Enter the 3rd integer: "))
if num1 == num2 or num1 == num3 or num2 == num3:
    sum_result = 0
else:
    sum_result = num1 + num2 + num3
print(f"Sum result: {sum_result}")
