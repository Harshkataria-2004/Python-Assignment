# Write a Python function to insert a string in the middle of a string

def insert_string_middle(string, string_to_insert):
    middle_index = len(string) // 2
    new_string = string[:middle_index] + string_to_insert + string[middle_index:]
    return new_string

print(insert_string_middle('aba','b'))