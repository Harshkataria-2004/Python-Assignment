# Write a Python program to create and display all combinations of letters,
# selecting each letter from a different key in a dictionary.
# o Sample data: {'1': ['a','b'], '2': ['c','d']} o Expected Output:
# o ac ad bc bd

data = {'1': ['a', 'b'], '2': ['c', 'd']}

combinations = []

for key, letters in data.items():
    if not combinations:
        combinations.extend(letters)
    else:
        new_combinations = []
        for combination in combinations:
            for letter in letters:
                new_combinations.append(combination + letter)
        combinations = new_combinations

for combo in combinations:
    print(combo)
