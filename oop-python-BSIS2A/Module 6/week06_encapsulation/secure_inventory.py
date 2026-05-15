class Product:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def get_product_info(self):
        print("Product:", self.__name)
        print("Price:", self.__price)
        print("Quantity:", self.__quantity)

    def update_quantity(self, quantity):
        if quantity >= 0:
            self.__quantity = quantity
        else:
            print("Invalid quantity")

    def update_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Invalid price")


product = Product("Laptop", 45000, 10)
product.get_product_info()

# Name: Bostero, Alexa C.