import json
from file_manager import user_manager, order_manager, admin_manager


class User:

    def __init__(self, user_name, email):
        self.user_name = user_name
        self.email = email
        self.my_balance = 0
        self.login = False

    def formatting_data(self):
        """This method is used to format input data in dict format"""
        return {
            'user_name': self.user_name,
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
            return False

    def add_order(self, count):
        self.create_order(count)
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
        else:
            for package in packages:
                pr = package['package_range']
                pr = pr.split('-')
                if count >= int(pr[0]) and count <= int(pr[1]):
                    return count * package[price]
                



user = User('zarina', "zarina@mail.ru")

user_manager.add_data(user.formatting_data())
user.add_balance(20, 15000)
user.add_order(15)
print(user.my_orders(), user.my_balance)
