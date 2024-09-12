import unittest
import json
import os
from main import regular_user

class TestRemoveItem(unittest.TestCase):
    def setUp(self):
        # Create a sample user and add some products to their cart
        self.user = regular_user(
            f_name="John",
            l_name="Doe",
            email="johndoe@example.com",
            password="password123",
            phone_number="1234567890",
            id=1,
            admin=False
        )
        self.user.products = [
            {"product": "Product1", "quantity": 2, "price": 10.0},
            {"product": "Product2", "quantity": 1, "price": 5.0}
        ]

        # Save the user data to a JSON file for testing
        with open("users.json", "w") as file:
            json.dump([self.user.__dict__], file, indent=2)

    def tearDown(self):
        # Remove the JSON file after testing
        if os.path.exists("users.json"):
            os.remove("users.json")

    def test_remove_item_not_found(self):
        # Remove an item that is not in the cart
        self.user.remove_item("Product3")

        # Load the updated user data from the JSON file
        with open("users.json", "r") as file:
            users_data = json.load(file)
        updated_user = users_data[0]

        # Assert that the product was not removed from the cart
        self.assertEqual(self.user.products, updated_user["products"])
        self.assertEqual("Product not found in your list.", self.user.remove_item.output)

if __name__ == "__main__":
    unittest.main()