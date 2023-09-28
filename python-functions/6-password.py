def validate_password(password):
    if len(password) < 8:
        return False
    if password.isalpha():
        return False
    if password.isdigit():
        return False
    if password.islower():
        return False
    if ' ' in password:
        return False
    else:
        return True
validate_password('Test@343777')