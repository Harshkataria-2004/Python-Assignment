# How do you perform pattern matching in Python? Explain 

import re
text = "The price of the product is $25.99"
pattern = r'\$\d+\.\d+'
match = re.search(pattern, text)
if match:
    print("Pattern found:", match.group())
