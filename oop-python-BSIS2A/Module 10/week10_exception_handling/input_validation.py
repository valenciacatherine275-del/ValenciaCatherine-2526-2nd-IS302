while True:
    try:
        number = int(input("Enter a number: "))
        break

    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("Valid number entered:", number)