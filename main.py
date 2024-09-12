from itertools import product
from tabnanny import check
from time import sleep
from functions import *
from user import User
from admin import Admin
from regular_user import regular_user
from Receipt import Receipt

filename = "Data.json"

email_completer = WordCompleter(get_emails(), ignore_case=True)


def main():
    Clean()
    print(Fore.BLUE+"Welcome to our system!"+Style.RESET_ALL)
    print(Fore.BLUE+"Please choose an option below:\n"+Style.RESET_ALL)
    while True:
        print("1. Register \t 2. Login \t 3. Exit")
        print(Fore.MAGENTA + 40 * '-' + Style.RESET_ALL)

        choice = input("Enter your choice: ")
        while choice not in ["1", "2", "3"]:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)
            choice = input("Enter your choice: ")

        if choice == "1":
            Clean()
            f_name = input("Enter your first name: ")
            l_name = input("Enter your last name: ")
            while not User.validate_name(f_name, l_name):
                print(Fore.RED + "First name and last name should have at least 2 characters." + Style.RESET_ALL)
                f_name = input("Enter your first name again: ")
                l_name = input("Enter your last name again: ")

            email = input("Enter your email: ")
            while User.in_validate_email(email):
                print("Please enter your email again: ")
                print(Fore.RED + "Please enter your email again: " + Style.RESET_ALL)
            user = find_user(email)
            while user is not None:
                print(Fore.RED + "User with this email already exists." + Style.RESET_ALL)
                email = input("Enter your email again: ")
                user = find_user(email)

            password = input_password()
            while not User.validate_password(password):
                print(Fore.RED + "Password should have at least 8 characters" + Style.RESET_ALL)
                password = input_password("Enter your password again: ")

            phone_number = input("Enter your phone number: ")
            while not User.validate_phone_number(phone_number):
                print(Fore.RED + "Phone number should have 11 characters" + Style.RESET_ALL)
                phone_number = input("Enter your phone number again: ")

            user = User(f_name, l_name, email, password, phone_number)
            Clean()
            user.save()
            if user.admin:
                print(Fore.GREEN + "You are registered as an Admin." + Style.RESET_ALL)
                Greeting_Admin(user.f_name)
                admin = Admin(
                    user.f_name,
                    user.l_name,
                    user.email,
                    user.password,
                    user.phone_number,
                    user.id,
                    user.admin,
                )
                adminMenu(admin)
            else:
                Clean()
                print(Fore.GREEN + "You are registered successfully." + Style.RESET_ALL)
                Regular_user = regular_user(
                    user.f_name,
                    user.l_name,
                    user.email,
                    user.password,
                    user.phone_number,
                    user.id,
                    user.admin,
                )
                userMenu(Regular_user)

        elif choice == "2":
            login()

        elif choice == "3":
            print("Exiting...")
            sleep(1)
            sys.exit()


def adminMenu(admin):
    print(f"Welcome to Admin Panel, {admin.name}!")
    print(Fore.MAGENTA + (len("Welcome to Admin Panel, {admin.name}!") + len({admin.name}) - 2) * '-' + Style.RESET_ALL)
    while True:
        print(Fore.BLUE+"1. Make a user an Admin\t\t2. Remove a user as an Admin\n"+Style.RESET_ALL)
        print(Fore.BLUE+"3. View all users\t\t4. View stats\n"+Style.RESET_ALL)
        print(Fore.BLUE+"5. Search for a user\t\t6. Delete a user\n"+Style.RESET_ALL)
        print(Fore.BLUE+"7. View your profile\t\t8. Change your password or User password\n"+Style.RESET_ALL)
        print(Fore.BLUE+"9. Add a new user\t\t10. Exit")
        print(Fore.MAGENTA + (len("9. Add a new user\t\t10. Exit") + 8 + 4) * '-' + Style.RESET_ALL)

        choice = input("Enter your choice: ")
        while choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)
            choice = input("Enter your choice: ")

        if choice == "1":
            Clean()
            admin.Make_Admin()
        elif choice == "2":
            Clean()
            admin.Remove_Admin()
        elif choice == "3":
            Clean()
            admin.view_users()
        elif choice == "4":
            Clean()
            admin.view_stats()
        elif choice == "5":
            Clean()
            admin.search_user()
        elif choice == "6":
            Clean()
            admin.delete_user()
        elif choice == "7":
            Clean()
            admin.view_profile()
        elif choice == "8":
            Clean()
            admin.change_password()
        elif choice == "9":
            Clean()
            admin.add_User()
        elif choice == "10":
            Clean()
            print("Back to login screen.")
            break


def userMenu(regular_user):
    print(f"Welcome {regular_user.name} on User's Panel !")
    print(Fore.MAGENTA + 26 * '-' + len(regular_user.name) * '-' + Style.RESET_ALL)
    while True:
        print(Fore.BLUE+"1. View your profile" + Style.RESET_ALL)
        print(Fore.BLUE+"2. Edit your profile"+ Style.RESET_ALL)
        print(Fore.BLUE+"3. Add an item to the cart"+ Style.RESET_ALL)
        print(Fore.BLUE+"4. Remove an item from the cart"+ Style.RESET_ALL)
        print(Fore.BLUE+"5. Update quantity of an item in the cart"+ Style.RESET_ALL)
        print(Fore.BLUE+"6. View your cart"+ Style.RESET_ALL)
        print(Fore.BLUE + "7. Calculate Total" + Style.RESET_ALL)
        print(Fore.BLUE + "8. Number of Items" + Style.RESET_ALL)
        print(Fore.BLUE + "9. Clear Cart" + Style.RESET_ALL)
        print(Fore.BLUE+"10. Check out"+ Style.RESET_ALL)
        print(Fore.BLUE + "11. Exit" + Style.RESET_ALL)

        choice = input("Enter your choice: ")
        while choice not in [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "13",
        ]:
            print("Invalid choice. Please try again.")
            choice = input("Enter your choice: ")

        if choice == "1":
            Clean()
            regular_user.view_profile()
        elif choice == "2":
            Clean()

            regular_user.edit_profile()
        elif choice == "3":
            Clean()

            name = input(
                Fore.YELLOW + "Enter Product Name: " + Style.RESET_ALL
            ).capitalize()
            while not name.isalpha():
                name = input(
                    Fore.RED + "Invalid name, Enter Product name: " + Style.RESET_ALL
                )
            price = input(Fore.YELLOW + "Enter Product Price: " + Style.RESET_ALL)
            while True:
                try:
                    price = float(price)
                    if price < 0:
                        raise ValueError
                    break
                except ValueError:
                    price = input(
                        Fore.RED
                        + "Invalid price, Enter Product Price: "
                        + Style.RESET_ALL
                    )
            quantity = int(
                input(Fore.YELLOW + "Enter Product Quantity: " + Style.RESET_ALL)
            )
            while True:
                try:
                    quantity = int(quantity)
                    if quantity < 0:
                        raise ValueError
                    break
                except ValueError:
                    quantity = input(
                        Fore.RED
                        + "Invalid quantity, Enter Product quantity: "
                        + Style.RESET_ALL
                    )
            regular_user.add_item(name, quantity, price)

        elif choice == "4":
            Clean()

            name = input(
                Fore.YELLOW + "Enter Product Name to remove: " + Style.RESET_ALL
            ).capitalize()
            while not name.isalpha():
                name = input(
                    Fore.RED
                    + "Invalid name, Enter Product Name to remove: "
                    + Style.RESET_ALL
                )
            regular_user.remove_item(name)
        elif choice == "5":
            Clean()

            name = input(
                Fore.YELLOW + "Enter Product Name to update: " + Style.RESET_ALL
            ).capitalize()
            while not name.isalpha():
                name = input(
                    Fore.RED
                    + "Invalid name, Enter Product Name to update: "
                    + Style.RESET_ALL
                )
            new_quantity = int(
                input(Fore.YELLOW + "Enter new Product Quantity: " + Style.RESET_ALL)
            )
            while True:
                try:
                    new_quantity = int(new_quantity)
                    if new_quantity < 0:
                        raise ValueError
                    break
                except ValueError:
                    new_quantity = input(
                        Fore.RED
                        + "Invalid quantity, Enter Product quantity: "
                        + Style.RESET_ALL
                    )
            regular_user.update_quantity(
                name, new_quantity, regular_user.get_quantity(name)
            )
        elif choice == "6":
            Clean()
            regular_user.view_cart()

        elif choice == "7":
            Clean()
            print(f"Total Price: {regular_user.calc_total_price()}\n")

        elif choice == "8":
            Clean()

            print(f"Number of Items: {regular_user.calc_number_of_items()}\n")
        elif choice == "9":
            Clean()

            regular_user.clear_cart()
        elif choice == "10":
            Clean()

            Receipt(regular_user, regular_user.name)
        elif choice == "11":
            Clean()

            print("thank you for using or system ... going back to login screen\n")
            break


def login():
    Clean()
    email = prompt("Enter your email: ", completer=email_completer)

    # Loop until a valid and existing email is entered
    while User.in_validate_email(email) or find_user(email) is None:
        if find_user(email) is None:
            print("User with this email does not exist. Please enter a valid email.")
        else:
            print("Invalid email format. Please try again.")
        email = prompt("Enter your email: ", completer=email_completer)

    password = prompt("Enter your password: ", is_password=True)
    password_correct = False

    user = find_user(email)
    # todo try and catch errors and exceptions
    while not password_correct:
        user = find_user(email)
        if user is not None and user["password"] == password:
            password_correct = True
        else:
            print(Fore.RED + "Invalid password." + Style.RESET_ALL)
            choice = input("Do you want to rewrite the password? (y/n): ")
            while choice.lower() not in ["y", "n"]:
                print("Invalid choice. Please try again.")
                choice = input("Do you want to rewrite the password? (y/n): ")
            if choice.lower() == "y":
                password = input_password("Enter your password again: ")
            else:
                break
    if user is None:
        print("User not found.")
    elif user["password"] != password:
        print(Fore.RED + "Invalid password." + Style.RESET_ALL)
    else:
        if user["admin"]:
            print(Fore.GREEN + "You are logged in as an Admin." + Style.RESET_ALL)
            f_name = user["name"].split()[0]
            l_name = user["name"].split()[1]
            admin1 = Admin(
                f_name,
                l_name,
                user["email"],
                user["password"],
                user["phone_number"],
                user["id"],
                user["admin"],
            )
            adminMenu(admin1)
        else:
            f_name = user["name"].split()[0]
            l_name = user["name"].split()[1]
            Regular_user = regular_user(
                f_name,
                l_name,
                user["email"],
                user["password"],
                user["phone_number"],
                user["id"],
                user["admin"],
            )

            userMenu(Regular_user)
            print(Fore.GREEN + "You are logged in as a regular user." + Style.RESET_ALL)


if __name__ == "__main__":
    main()
