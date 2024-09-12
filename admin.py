from user import *
import json
from functions import *
filename = "Data.json"

class Admin(User):
    def __init__(self, f_name, l_name, email, password, phone_number, id, admin):
        super().__init__(f_name, l_name, email, password, phone_number)
        self.admin = True

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
                }
            )
            json.dump(users, file, indent=2)
            print("Admin saved successfully.")

    def Make_Admin(self):
        with open(filename, "r") as file:
            users_data = json.load(file)
        email = input("Enter the email of the user you want to make an admin: ")
        for user in users_data:
            if user["email"] == email:
                user["admin"] = True
                break
        else:
            print("User not found.")
            return

        with open(filename, "w") as file:
            json.dump(users_data, file, indent=2)
        print(f"{email} is now an Admin.")
        print((len(f"{email} is now an Admin.")+6)*"-")
            

    def Remove_Admin(self):
        with open(filename, "r") as file:
            users_data = json.load(file)
        email = input("Enter the email of the user you want to make an admin: ")
        for user in users_data:
            if user["email"] == email:
                user["admin"] = False
                break
        else:
            print("User not found.")
            return

        with open(filename, "w") as file:
            json.dump(users_data, file, indent=2)
        print(f"{email} is now not an Admin.")
        print((len(f"{email} is now an Admin.")+6)*"-")
        

    def view_users(self):
        users = load_users(filename)
        for user in users:
            print(user)
            print(30 * "-")
    def view_stats(self):
        total_users = len(load_users(filename))
        admin_users = sum([1 for user in load_users(filename) if user["admin"]])
        print(f"Total users: {total_users}")
        print(f"Admin users: {admin_users}")
        print((len(f"Admin users: {admin_users}")+6)*"-")

    def search_user(self):
        email = input("Enter the email of the user you want to search: ")
        user = find_user(email)
        if user is None:
            print("User not found.")
        else:
            print(user)
            print(30 * "-")

    def delete_user(self):
        email = input("Enter the email of the user you want to delete: ")
        user = find_user(email)
        if user is None:
            print("User not found.")
        else:
            users = load_users(filename)
            users.remove(user)
            with open(filename, "w") as file:
                json.dump(users, file, indent=2)
                print(f"{user['name']} has been deleted.")
                print((len(f"{user['name']} has been deleted.")+6)*"-")

    def view_profile(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone Number: {self.phone_number}")
        print(f"ID: {self.id}")
        if self.admin:
            print("Admin: Yes")
            print(30 * '-')
        else:
            print("Admin: No")
            print(30 * '-')
            

    def change_password(self):
        with open(filename, "r") as file:
            users_data = json.load(file)
        email = input("Enter the email of the user you want to make an admin: ")
        for user in users_data:
            if user["email"] == email:
                new_password = input_password("Enter your new password: ")
                user["password"] = new_password
                break
        else:
            print("User not found.")
            return

        with open(filename, "w") as file:
            json.dump(users_data, file, indent=2)
        print(f"The password of the {email} has changed .")
        print((len(f"The password of the {email} has changed .")+6)*"-")
        
    def add_User(self):
        f_name = input("Enter your first name: ")
        l_name = input("Enter your last name: ")
        email = input("Enter your email: ")
        while User.in_validate_email(email):
            print("Invalid email. Please try again.")
            email = input("Enter your email: ")
        while find_user(email) is not None:
            print("Email already exists. Please try again.")
            email = input("Enter your email: ")
        password = input_password()
        while not User.validate_password(password):
            print("Password must be at least 8 characters long. Please try again.")
            password = input_password()
        phone_number = input("Enter your phone number: ")
        while not User.validate_phone_number(phone_number):
            print("Invalid phone number. Please try again.")
            phone_number = input("Enter your phone number: ")
        user = User(f_name, l_name, email, password, phone_number)
        user.save()
