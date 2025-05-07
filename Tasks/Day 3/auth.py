DataBase = [
    {"name": "mahmoud", "password": "123"},
    {"name": "atef", "password": "456"}
]

def login():
    try:
        name = input("Please Enter Your Username: ").strip()

        if not name.isalpha():
            print("Please enter a valid username (letters only).")
            return

        user = next((user for user in DataBase if user["name"] == name), None)

        if user:
            password = input("Please Enter Your Password: ").strip()
            if password == user["password"]:
                print(f"Welcome, {name}!")
            else:
                print("Wrong password!")
        else:
            print("Error: Unregistered user.")

    except KeyboardInterrupt:
        print("\nLogin canceled by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
