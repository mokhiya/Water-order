from file_manager import JsonManager, admin_manager

def see_all_users():
    user_manager = JsonManager("users.json")
    users = user_manager.read_data()

    if not users:
        print("There is no any users")
    else:
        print("\nList of all registered users:")
        print("Username                 | Email")
        print("═══════════════════════════════════════════")
        for user in users:
            print(f"{user['user_name']} | {user['email']}")


def create_water_package():
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
