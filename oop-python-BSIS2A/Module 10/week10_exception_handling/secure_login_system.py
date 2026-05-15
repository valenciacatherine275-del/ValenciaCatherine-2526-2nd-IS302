try:
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Input validation
    if username == "" or password == "":
        raise ValueError("Username and password cannot be empty")

    # Try to open users file
    try:
        with open("users.txt", "r") as file:
            users = file.readlines()

    except FileNotFoundError:
        print("Error: users.txt file not found")
        exit()

    login_success = False

    # Check credentials
    for user in users:
        stored_user, stored_pass = user.strip().split(",")

        if username == stored_user and password == stored_pass:
            login_success = True
            break

    if login_success:
        print("Login successful!")
    else:
        print("Invalid username or password")

except ValueError as ve:
    print("Input Error:", ve)

except Exception as e:
    print("Unexpected error:", e)

finally:
    print("Login process finished.")