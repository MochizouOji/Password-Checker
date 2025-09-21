def check_length(password):
    return len(password) >= 6

def count_characters(password):
    upper_chars = sum(1 for c in password if c.isupper())
    lower_chars = sum(1 for c in password if c.islower())
    digits = sum(1 for c in password if c.isdigit())
    special_chars = sum(1 for c in password if not c.isalnum())
    return upper_chars, lower_chars, digits, special_chars

def password_strength(password):
    length = len(password)
    upper_chars, lower_chars, digits, special_chars = count_characters(password)

    if not check_length(password):
        return "Password must be at least 6 characters long!"

    feedback = []

    if upper_chars == 0:
        feedback.append("Password must contain at least one uppercase character!")
    if lower_chars == 0:
        feedback.append("Password must contain at least one lowercase character!")
    if special_chars == 0:
        feedback.append("Password must contain at least one special character!")
    if digits == 0:
        feedback.append("Password must contain at least one digit!")

    if feedback:
        return "\n".join(feedback)
    
    if length >= 10:
        return "The strength of the password is strong."
    else:
        return "The strength of the password is medium."

def check_password(password):
    feedback = password_strength(password)
    print(feedback)

password = input("Please enter password: ")
check_password(password)
