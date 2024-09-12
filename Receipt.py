from functions import *
class Receipt:
    def __init__(self, cart, customer_name):
        self.cart = cart
        self.customer_name = customer_name
        self.total_price = cart.calc_total_price()
        self.number_of_items = cart.calc_number_of_items()
        self.display_receipt()

    def display_receipt(self):
        print(Fore.CYAN + "Receipt" + Style.RESET_ALL)
        print(Fore.MAGENTA + "---" * 10 + Style.RESET_ALL)
        print(
            Fore.YELLOW
            + f"Date: {datetime.now().strftime('%Y-%m-%d')}"
            + Style.RESET_ALL
        )
        print(Fore.YELLOW + f"Customer: {self.customer_name}" + Style.RESET_ALL)
        print(Fore.MAGENTA + "---" * 10 + Style.RESET_ALL)
        print(Fore.GREEN + "Product\t\tQuantity\tPrice\t\tTotal" + Style.RESET_ALL)

        for product in self.cart.current_user["products"]:
            print(
                Fore.GREEN
                + f"{product['product']}\t\t{product['quantity']}\t\t{product['price']}\t\t{product['total']}"
                + Style.RESET_ALL
            )

        print(Fore.MAGENTA + "---" * 10 + Style.RESET_ALL)
        print(Fore.RED + f"Total Price: {self.total_price}" + Style.RESET_ALL)
        print(Fore.CYAN + f"Number of Items: {self.number_of_items}" + Style.RESET_ALL)
        print(Fore.MAGENTA + "---" * 10 + Style.RESET_ALL)