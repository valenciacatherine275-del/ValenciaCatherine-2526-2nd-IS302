# Name: Bostero, Alexa C.

product = input("Enter product name: ")
price = input("Enter price: ")

with open("inventory.txt", "a") as file:
    file.write(product + "," + price + "\n")

print("Product saved successfully.")

print("\nInventory List:")
with open("inventory.txt", "r") as file:
    for line in file:
        print(line.strip())