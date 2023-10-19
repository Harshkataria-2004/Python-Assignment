# Write a Python program to count the number of characters (character
# frequency) in a string

string = input("Enter a string: ")
freq = {}
for char in string:
    if char != ' ':
        freq[char] = freq.get(char, 0) + 1

for char, count in freq.items():
    print(char," : ",count)
