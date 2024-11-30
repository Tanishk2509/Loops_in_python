import string

def is_valid_password(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in string.punctuation:
            has_special = True
    
    if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
        return True
    else:
        return False
password = input("Enter your password: ")

if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid. i must be spacial char, ")