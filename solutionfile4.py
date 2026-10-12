# Password Validator
# Write a Python program that validates a user's password.

# A password is considered valid if:
# It contains at least 8 characters
# It contains at least one uppercase letter
# It contains at least one lowercase letter
# It contains at least one digit

# The program should display whether the password is valid or invalid.


password = input("Enter password: ")

has_upper = False
has_lower = False
has_digit = False

if password > 8:

    for char in password:
        if chr.has_upper():
            has_upper == True

        elif chr.has_lower():
            has_lower == True

        elif chr.has_digit():
            has_digit = False

    if has_upper or has_lower or has_digit:
        print("Valid Password")
    else:
        print("Invalid Password")
else:
    print("Invalid Password")
