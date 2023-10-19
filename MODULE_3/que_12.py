# Write a Python function that takes a list and returns a new list with unique
# elements of the first list. 

def unique_elements(input_list):
    unique_set = set()
    for item in input_list:
        unique_set.add(item)
    unique_list = list(unique_set)   
    return unique_list
input_list = [1, 2, 2, 3, 4, 4, 5]
result = unique_elements(input_list)
print(result)
