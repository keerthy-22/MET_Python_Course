class Book:
    def __init__(self, title, author, isbn, price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price

    def display_info(self):
        print("\n------ Book Details ------")
        print("Title  :", self.title)
        print("Author :", self.author)
        print("ISBN   :", self.isbn)
        print("Price  : ₹", self.price)

    def apply_discount(self, discount_percent):
        discount_amount = (self.price * discount_percent) / 100
        self.price = self.price - discount_amount
        print("\nDiscount Applied:", discount_percent, "%")
        print("New Price: ₹", self.price)


# User Input
title = input("Enter Book Title: ")
author = input("Enter Author Name: ")
isbn = input("Enter ISBN Number: ")
price = float(input("Enter Book Price: "))

# Create Object
book1 = Book(title, author, isbn, price)

# Display Book Details
book1.display_info()

# Apply Discount
discount = float(input("\nEnter Discount Percentage: "))
book1.apply_discount(discount)

# Display Updated Details
book1.display_info()
