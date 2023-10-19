# Write a Python program to test whether a passed letter is a vowel or not

user= input("Enter a letter: ").lower()
if len(user) == 1 and user.isalpha():
    if user in "aeiou":
        print(f"{user} is a vowel.")
    else:
        print(f"{user} is not a vowel.")
else:
    print("Enter a single letter.")
