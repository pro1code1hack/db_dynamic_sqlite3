"""

ord()

"""


def hash_password(password):
    new_password = ""

    for letter in password:
        new_password += str(ord(letter))
    
    return new_password