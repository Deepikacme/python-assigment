class InvalidLoginError(Exception):
    pass

class LoginSystem:
    def login(self, username, password):
        if username != "admin" or password != "1234":
            raise InvalidLoginError("Invalid username or password")
        print("Login successful")

try:
    l = LoginSystem()
    l.login("user", "1111")
except InvalidLoginError as e:
    print(e)