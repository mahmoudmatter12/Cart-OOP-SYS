from user import User
filename = "Data.json"
import json

class regular_user(User):
    def __init__(self, f_name, l_name, email, password, phone_number, id, admin):
        super().__init__(f_name, l_name, email, password, phone_number)
        self.admin = False
        self.current_user = self.load_current_user()

    def get_quantity(self, product_name):
        if self.current_user is None:
            print("Current user not found.")
            return
        for product in self.current_user["products"]:
            if product["product"] == product_name:
                return int(product["quantity"])  # Return the quantity of the specified product
    
    def save_current_user_data(self):
    # Load all users' data from the file
        with open(filename, "r") as file:
            users_data = json.load(file)

    # Find the current user and update their data
        for i, user in enumerate(users_data):
            if user["email"] == self.email:
                users_data[i] = self.current_user
                break

    # Save the updated data back to the JSON file
        with open(filename, "w") as file:
            json.dump(users_data, file, indent=2)      
        print("Current user data saved successfully.\n")

    def load_current_user(self):
        # Load all users' data from the file
        with open(filename, "r") as file:
            users_data = json.load(file)

        # Find the current logged-in user
        for user in users_data:
            if user["email"] == self.email:
                return user
        
        # If user not found, return None
        print("Current user not found.")
        return None
 
    def view_profile(self):
        print(f"Name: \t\t{self.name}")
        print(f"Email: \t\t{self.email}")
        print(f"Phone Number: \t{self.phone_number}")
        print(f"ID: \t\t{self.id}")
        print(f"Admin: \t\t{self.admin}")
        print((len("Admin: \t\t{self.admin}")+6)*"-")

    def edit_profile(self):
        print(
            "You are not an admin. You cannot edit your profile. pleas contact the admin.\n"
        )
        with open(filename, "r") as file:
            users_data = json.load(file)
        admin_list = []
        for user in users_data:
            if user["admin"]:
                admin_list.append(user["name"])
        if len(admin_list) == 0:
            print("No admins found.")
            print((len("No admins found."))*"-")
            return
        else:
            print("Admins: ")
            for admin_name in admin_list:
                print(admin_name)
            print((len("No admins found."))*"-")

    def add_item(self, product, quantity, price):
        if self.current_user is None:
            print("No valid user found. Please login first. \n")
            return

        self.current_user["products"].append(
            {"product": product, "quantity": quantity, "price": price , "total": 0+quantity*price}
            )

        self.save_current_user_data()

        print(f"{product} has been added to your list with quantity={quantity} and price={price}.")
        print((len("{product} has been added to your list with quantity={quantity} and price={price}."))*'-')

    def remove_item(self, product_name):
        if self.current_user is None:
            print("Current user not found. \n")
            return

        # Check if the product exists in the current user's product list
        for product in self.current_user["products"]:
            if product["product"] == product_name:
                self.current_user["products"].remove(product)
            break
        else:
            print("Product not found in your list. \n")
            return

        self.save_current_user_data()

        print(f"{product_name} has been removed from your list.")
        print((len("{product_name} has been removed from your list."))*'-')

    def update_quantity(self, product_name, new_quantity,quantity):
        if self.current_user is None:
            print("Current user not found.\n")
            return

    # Check if the product exists in the current user's product list
        for product in self.current_user["products"]:
            if product["product"] == product_name:
            # Update the quantity for the matched product
                product["quantity"] = new_quantity  
            
            # Update the total price based on the new quantity and price
                product["total"] = new_quantity * product["price"]
                break
        else:
            print("Product not found in your list.\n")
            return

    # Save the updated user data back to the file
        self.save_current_user_data()

        print(f"Quantity of {product_name} has been updated to from {quantity} to {new_quantity}. Total price: {product['total']}")
        print((len(f"Quantity of {product_name} has been updated to from {quantity} to {new_quantity}. Total price: {product['total']}")*'-'))

    def calc_total_price(self):
        if self.current_user is None:
            print("Current user not found.")
            return
        return sum([product["total"] for product in self.current_user["products"]])
    
    def view_cart(self):
        if self.current_user is None:
            print("Current user not found.")
            return

        print("Your shopping cart:")
        for product in self.current_user["products"]:
            print(f"{product['product']:<20}\tQuantity: {product['quantity']:<5}\tPrice: {product['price']:<8}\tTotal: {product['total']:<8}\n")
        print(f"Total Price: {self.calc_total_price()}")
        print()
    
    def calc_number_of_items(self):
        if self.current_user is None:
            print("Current user not found.")
            return
        return len(self.current_user["products"])

    def clear_cart(self):
        if self.current_user is None:
            print("Current user not found.")
            return

        self.current_user["products"] = []
        self.save_current_user_data()

        print("Cart has been cleared.")
        print()
    