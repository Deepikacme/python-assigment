class InvalidPasswordError(Exception):
    pass
    password = input("Enter password: ")

    if len(password) < 8:
        raise InvalidPasswordError("Password is too short")

    print("Valid password")
    print(e)