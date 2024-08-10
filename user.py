import json
from file_manager import user_manager, order_manager, admin_manager


class User:

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.my_balance = 0
        self.login = False

    def formatting_data(self):
        """This method is used to format input data in dict format"""
        return {
            'username': self.username,
            'email': self.email,
            'login': self.login,
            'balance': self.my_balance
        }

    def add_balance(self, count):
        total = self.total_price(count)
        if total:
            print(f"Total price will be:  {total}")
            answer = input("Do you add balance?  y/n:  ").lower()
            if answer == 'y':
                self.my_balance += count

    def create_order(self, count):
        if count <= self.my_balance:
            self.my_balance -= count
            return True
        else:
            diff = count - self.my_balance
            print(f"You need to add {diff} water to your balance.")
            answer = input("Do you want to add?  y/n").lower()
            if answer == 'y':
                self.add_balance(diff)
                self.my_balance = 0
                return True
            else:
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

    @staticmethod
    def total_price(count):
        packages = admin_manager.read_data()
        if not packages:
            print("There are no packages yet.")
            return None

        for package in packages:
            pr = package['package_range']
            pr = pr.split('-')
            if int(pr[0]) <= count <= int(pr[1]):
                return count * package['price']

        return None
