from user import User

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

    user.add_onedata_to_file(user.formatting_order())
    return display_menu()