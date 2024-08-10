import json
from file_manager import user_manager, order_manager

class User():
    
    def __init__(self, user_name, email, file_name="users.json"):
        super().__init__(file_name)
        self.user_name = user_name
        self.email = email
        self.my_balance = 0
        self.login = False

    def add_order(self, order):
        """This method is used to add other team members to the list"""
        self.orders.append(order)

    def formatting_data(self):
        """This method is used to format input data in dict format"""
        return {
            'user_name': self.user_name,
            'email': self.email,
            'login': self.login,
            'balance': self.my_balance
        }

    def add_balance(self, count, price):
        total = count * price
        print(f"Total price will be:  {total}")
        answer = input("Do you wont to add balance?  y/n:  ").lower()
        if answer == "y":
            self.my_balance += count

    def create_order(self, count):
        if self.my_balance >= count:
            self.my_balance -= count
            return True
        return False

    def add_order(self, count):
        if self.create_order(count):
            order = {
                'user_email': self.email,
                'water quantity': count
            }
            order_manager.add_data(order)

    def my_orders(self):
        orders = order_manager.read()

        for order in orders:
            if order['user_email'] == self.email:
                yield order
