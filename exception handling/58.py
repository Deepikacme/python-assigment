class InvalidPasswordError(Exception):
    pass

def password_check(password):
        if len(password)<8:
            raise InvalidPasswordError("Password is too short")

        print("Valid password")
        print(not len(password)<8)
password_check("hello")