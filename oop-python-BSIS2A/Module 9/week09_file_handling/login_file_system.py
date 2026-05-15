# Name: Bostero, Alexa C.

def register():
    username = input("Enter new username: ")
    password = input("Enter new password: ")

    with open("users.txt", "a") as file:
        file.write(username + "," + password + "\n")

    print("User registered successfully.\n")


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("users.txt", "r") as file:
        users = file.readlines()

    for user in users:
        data = user.strip().split(",")

        if data[0] == username and data[1] == password:
            print("Login successful!")
            return

    print("Invalid username or password.")


while True:
    print("\n=== LOGIN SYSTEM ===")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")