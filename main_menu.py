from registration import check_user, check_admin, register_user


def show_admin_menu():
    while True:
        text = input("""
1. See all users.
2. See orders.
3. Create/Update package.
4. Logout.

Choose an option above: """).strip()

        if text == '1':
            pass
        elif text == '2':
            pass
        elif text == '3':
            pass
        elif text == '4':
            show_auth_menu()
        else:
            print("Invalid input, try again")


def show_user_menu():
    text = """
    1. Fill my balance.
    2. Order water.
    3. Orders history.
    4. Logout.
    """
    print(text)

    user_input = input("Choose an option above: ").strip()

    if user_input == "1":
        pass
    elif user_input == "2":
        pass
    elif user_input == "3":
        pass
    elif user_input == "4":
        pass
    else:
        print("Invalid input, try again")


def show_auth_menu():
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
        username = input("Enter a username: ").strip()
        password_or_email = input("Enter an email or a password: ").strip()
        if check_admin(username=username, password=password_or_email):
            print("You have successfully logged in.")
            show_admin_menu()
        elif check_user(username=username, email=password_or_email):
            print("You have successfully logged in.")
            show_user_menu()
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
        return show_admin_menu()


if __name__ == '__main__':
    show_auth_menu()
