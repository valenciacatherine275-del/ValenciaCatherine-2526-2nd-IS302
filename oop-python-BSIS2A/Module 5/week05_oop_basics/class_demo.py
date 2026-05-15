# Name: Bostero, Alexa C.

class Person_acb:
    def __init__(self, name_acb, age_acb):
        self.name_acb = name_acb
        self.age_acb = age_acb

    def display_info_acb(self):
        print("Name:", self.name_acb)
        print("Age:", self.age_acb)


p1_acb = Person_acb("Juan", 20)
p1_acb.display_info_acb()