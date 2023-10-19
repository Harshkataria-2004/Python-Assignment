# Write a Python program to find the highest 3 values in a dictionary 

data = {'a': 10, 'b': 20, 'c': 15, 'd': 25, 'e': 5}
sorted_items = sorted(data.items(), key=lambda x: x[1], reverse=True)
top_3_values = sorted_items[:3]

for key, value in top_3_values:
    print(f'Key: {key}, Value: {value}')
