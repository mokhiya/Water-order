from user import User
from file_manager import user_manager


def register_user():
    """
    This function is used to register participants
    """
    user_name = input("Enter your full name: ").strip()

    while True:  # Validating email format
        user_email = input("Enter your email: ").strip()
        if user_email.endswith('@gmail.com') or user_email.endswith('@mail.ru') or user_email.endswith('@yahoo.com'):
            break
        else:
            print("Invalid input, enter an email again!")

    user = User(user_name=user_name, email=user_email)

    user.add_data(user.formatting_data())
    return True


def login_user(username, email):
    all_users = user_manager.read()
    for user in all_users:
        if user['user_name'] == username and user['email'] == email:
            return True
    return False


