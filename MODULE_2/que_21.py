# Write a Python program to get a string made of the first 2 and the last 2
# chars from a given a string. If the string length is less than 2, return
# instead of the empty string.
# o Sample String: w3resource' o
# Expected Result: 'w3ce' o Sample
# String: 'w3' o Expected Result:
# 'w3w3' o Sample String: ' w' o
# Expected Result: Empty String

def string_both_ends(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]

print(string_both_ends('Tops tech'))
print(string_both_ends('To'))
print(string_both_ends('w'))