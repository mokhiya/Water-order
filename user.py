import json

from file_manager import JsonManager
from contextlib import contextmanager


@contextmanager
def custom_open(file_name, mode):
    file = open(file_name, mode)
    yield file
    file.close()

class User(JsonManager):
    
    def __init__(self, user_name, email, file_name="users.json"):
        super().__init__(file_name)
        self.user_name = user_name
        self.email = email
        self.orders = []
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
            'orders': self.orders
        }

    def add_balance(self, count, price):
        total = count * price
        print(f"Total price:  {total}")
        answer = input("Do you wont to add balance?  (Yes or No):  ")
        if answer == "Yes":
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
                'count of water': count
            }
            with custom_open('orders.json', 'w') as file:
                json.dump(order, file)
