# Write a Python program to unzip a list of tuples into individual lists. 

list_of_tuples = [(1, 'one'), (2, 'two'), (3, 'three')]
numbers, words = zip(*list_of_tuples)
print("Numbers:", numbers)
print("Words:", words)