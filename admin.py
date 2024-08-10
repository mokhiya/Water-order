from file_manager import JsonManager

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


see_all_users()