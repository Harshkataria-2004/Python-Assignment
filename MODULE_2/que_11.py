# Write a python program to sum of the first n positive integers

n = int(input("Enter a value : "))
sum = 0
if n > 0:
    for i in range(1, n + 1):
        sum += i

    # Print the result
    print(sum)
else:
    print("Enter a positive number")
