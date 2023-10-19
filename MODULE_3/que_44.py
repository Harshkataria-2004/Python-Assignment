# Write a Python program to print all unique values in a dictionary.

my_dict = {'a': 1, 'b': 2, 'c': 2, 'd': 3, 'e': 1}
unique_values = set()
for value in my_dict.values():
    unique_values.add(value)
print("Unique values in the dictionary:")
for value in unique_values:
    print(value)
