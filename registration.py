from user import User
from file_manager import user_manager

admin_username = "admin"
admin_password = "0000"


def register_user():
    """
    This function is used to register participants
    """
    user_name = input("Enter a username: ").strip()

    while True:  # Validating email format
        user_email = input("Enter your email: ").strip()
        if user_email.endswith('@gmail.com') or user_email.endswith('@mail.ru') or user_email.endswith('@yahoo.com'):
            break
        else:
            print("Invalid input, enter an email again!")

    user = User(user_name=user_name, email=user_email)
    user_manager.add_data(user.formatting_data())
    return True


def check_user(username, email):
    all_users = user_manager.read_data()
    for user in all_users:
        if user['username'] == username and user['email'] == email:
            user['login'] = True
            user_manager.write_data(all_users)
            return True
    return False


def check_admin(username, password):
    if username == admin_username and password == admin_password:
        return True
    return False
