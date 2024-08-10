from file_manager import JsonManager, admin_manager, order_manager, user_manager


def see_all_users():
    """
    Fetches and displays all registered users from 'users.json'.
    """
    users = user_manager.read_data()

    if not users:
        print("No users found.")
    else:
        print("\nList of all registered users:")
        print("{:<20} {:<30}".format("Ism", "Email"))
        print("-" * 50)
        for user in users:
            print("{:<20} {:<30}".format(user['user_name'], user['email']))


def print_package():
    """
    Prints the name of the admin and the available water packages with their ranges and prices.
    """
    data = admin_manager.read_data()
    print(f"Admin Name: {data['admin_name']}")
    print("Packages:")
    
    for package in data['packages']:
        print(f"  - Range: {package['package_range']}, Price: {package['price']}")


def create_water_package():
    """
    Prompts the admin to create new water packages and saves them to 'admin_data'.
    """
    admin_data = []
    package_quantity = int(input("How many packages do you want to create? "))

    for i in range(package_quantity):
        package = input("Enter a range between 1 and 100 for water bottles (ex: 1-10): ")
        price = float(input("Enter price for the package: "))

        admin_data.append({
            'package_range': package,
            'price': price
        })

    admin = {
        'admin_name': 'admin',
        'packages': admin_data
    }

    admin_manager.write_data(admin)
    print_package()


def see_all_orders():
    """
    Fetches and displays all user orders from 'orders.json'.
    """
    orders = order_manager.read_data()

    if not orders:
        print("No orders found.")
    else:
        print("\nUser Orders:")
        print("{:<30} {:<30}".format("Email", "Orders"))
        print("-" * 80)
        for user in orders:
            user_orders = user['orders']
            order_list = ", ".join(user_orders) if user_orders else "No orders"
            print("{:<30} {:<30}".format(user['email'], order_list))
