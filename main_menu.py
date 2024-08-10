from registration import check_user, check_admin, register_user
from admin import see_all_users, create_water_package, see_all_orders
from user import User
from file_manager import user_manager


def show_admin_menu():
    """
    This function shows the admin menu.
    """
    while True:
        text = input("""
1. See all users.
2. See orders.
3. Create/Update package.
4. Logout.

Choose an option above: """).strip()

        if text == '1':
            see_all_users()
            return show_admin_menu()
        elif text == '2':
            see_all_orders()
            return show_admin_menu()
        elif text == '3':
            create_water_package()
            return show_admin_menu()
        elif text == '4':
            print("You have logged out")
            show_auth_menu()
        else:
            print("Invalid input, try again")


def show_user_menu(user):
    """
    This function shows the user menu.
    """
    text = """
    1. Fill my balance.
    2. Order water.
    3. Orders history.
    4. Logout.
    """
    print(text)

    user_input = input("Choose an option above: ").strip()

    if user_input == "1":
        print("How many water do you want to add to your balance?")
        quantity = int(input("Enter an integer:  "))
        user.add_balance(quantity)
        user_manager.update_data(user.user_name, 'username', user.formatting_data())
        show_user_menu(user)
    elif user_input == "2":
        quantity = int(input("How many water would you like to order?"))
        user.add_order(quantity)
        user_manager.update_data(user.user_name, 'username', user.formatting_data())
        show_user_menu(user)
    elif user_input == "3":
        print(list(user.my_orders()))
        show_user_menu(user)
    elif user_input == "4":
        user.login = False
        user_manager.update_data(user.user_name, 'username', user.formatting_data())
        show_auth_menu()
    else:
        print("Invalid input, try again")


def show_auth_menu():
    """
    This function shows the auth menu.
    """
    text = """
1. Register.
2. Log in.
3. Exit.
"""
    print(text)

    user_input = input("Choose an option above: ").strip()

    if user_input == "1":
        if register_user():
            print("You have successfully registered.")
        else:
            print("Something went wrong, try again!")
        return show_auth_menu()

    elif user_input == "2":
        username = input("Enter your username: ").strip()
        password_or_email = input("Enter an email or a password: ").strip()
        if check_admin(username=username, password=password_or_email):
            print("You have successfully logged in.")
            show_admin_menu()
        elif check_user(username=username, email=password_or_email):
            print("You have successfully logged in.")
            user = User(username, password_or_email)
            show_user_menu(user)
        else:
            print("System cannot detect you, please try again!")
            show_auth_menu()
    elif user_input == "3":
        yes_no_input = input("Would you like to quit? (y/n): ")
        if yes_no_input.lower() == "y":
            print("You quit the program. See you!")
        else:
            return show_auth_menu()
    else:
        print("Choose a proper number! ")
        return show_auth_menu()


if __name__ == '__main__':
    show_auth_menu()
