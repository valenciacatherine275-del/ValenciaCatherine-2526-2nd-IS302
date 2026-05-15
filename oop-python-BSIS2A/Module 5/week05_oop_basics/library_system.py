# Name: Bostero, Alexa C.

class Book_acb:
    def __init__(self, title_acb, author_acb, year_acb):
        self.title_acb = title_acb
        self.author_acb = author_acb
        self.year_acb = year_acb

    def display_book_acb(self):
        print("Title:", self.title_acb)
        print("Author:", self.author_acb)
        print("Year:", self.year_acb)
        print()


# Create 3 book objects
book1_acb = Book_acb("Python Programming", "John Smith", 2022)
book2_acb = Book_acb("Data Structures", "Jane Doe", 2021)
book3_acb = Book_acb("OOP Concepts", "Mark Lee", 2023)

# Display books
book1_acb.display_book_acb()
book2_acb.display_book_acb()
book3_acb.display_book_acb()