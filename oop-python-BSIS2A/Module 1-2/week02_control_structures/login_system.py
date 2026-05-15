correct_username_acb = "admin"
correct_password_acb = "1234"

attempts = 0

while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username_acb and password == correct_password_acb:
        print("Login Successful")
        break
    else:
        print("Invalid Credentials")
        attempts += 1

if attempts == 3:
    print("Account Locked")