# Write python program that swap two number with temp variable and without temp variable.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

temp = num1
num1 = num2
num2 = temp

print("After swapping (with temp variable):")
print("First number:", num1)
print("Second number:", num2)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("After swapping (without temp variable):")
print("First number:", num1)
print("Second number:", num2)
