# Write a Python script to sort (ascending and descending) a dictionary by
# value. 

sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}
sorted_dict_ascending = dict(sorted(sample_dict.items(), key=lambda item: item[1]))
sorted_dict_descending = dict(sorted(sample_dict.items(), key=lambda item: item[1], reverse=True))
print("Ascending Order:")
print(sorted_dict_ascending)

print("\nDescending Order:")
print(sorted_dict_descending)
