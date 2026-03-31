import re

password = input("Enter a password: ")

length = len(password) >= 8
uppercase = re.search("[A-Z]", password)
lowercase = re.search("[a-z]", password)
number = re.search("[0-9]", password)
symbol = re.search("[@#$%^&*!]", password)

score = sum([bool(length), bool(uppercase), bool(lowercase), bool(number), bool(symbol)])

if score <= 2:
    print("Weak Password ❌")
elif score == 3 or score == 4:
    print("Medium Password ⚠️")
else:
    print("Strong Password ✅")