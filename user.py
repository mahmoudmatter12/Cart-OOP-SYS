from functions import *
filename = "Data.json"

class User:

    def __init__(self, f_name, l_name, email, password, phone_number):
        self.f_name = f_name
        self.l_name = l_name
        self.name = f_name + " " + l_name
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.id = randint(1000, 10000)
        self.admin = User.check_admin(email)
        self.products = []

    @staticmethod
    def validate_password(password):
        if len(password) < 8:
            return False
        return True

    @staticmethod
    def in_validate_email(email):
        if email == "admin":
            return False
        if "@" not in email or "." not in email:
            return True
        return False

    @staticmethod
    def validate_phone_number(phone_number):
        if len(phone_number) != 11:
            return False
        return True

    @staticmethod
    def validate_name(f_name, l_name):
        if len(f_name) < 2 or len(l_name) < 2:
            return False
        return True

    @staticmethod
    def check_admin(email):
        if email == "admin":
            return True
        return False

    def save(self):
        try:
            with open(filename, "r") as file:
                users = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            users = []

        with open(filename, "w") as file:
            users.append(
                {
                    "name": self.name,
                    "email": self.email,
                    "password": self.password,
                    "phone_number": self.phone_number,
                    "id": self.id,
                    "admin": self.admin,
                    "products": self.products,
                }
            )
            json.dump(users, file, indent=2)
            print("User saved successfully.")
