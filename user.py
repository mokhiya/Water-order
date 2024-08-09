from file_manager import JsonManager


class User(JsonManager):

    def __init__(self, user_name, email, file_name="users.json"):
        super().__init__(file_name)
        self.user_name = user_name
        self.email = email
        self.orders = []
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
