# Name: Bostero, Alexa C.

class Car_acb:
    def __init__(self, brand_acb, model_acb, year_acb):
        self.brand_acb = brand_acb
        self.model_acb = model_acb
        self.year_acb = year_acb

    def display_car_acb(self):
        print(self.brand_acb, self.model_acb, self.year_acb)


car1_acb = Car_acb("Toyota", "Corolla", 2020)
car1_acb.display_car_acb()