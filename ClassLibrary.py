class LibraryBook:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
        self.borrower = "None"

    def issue_book(self, borrower_name):
        if self.available:
            self.available = False
            self.borrower = borrower_name
            print("\nBook issued successfully.")
        else:
            print("\nBook is already issued to", self.borrower)

    def return_book(self):
        if not self.available:
            self.available = True
            self.borrower = "None"
            print("\nBook returned successfully.")
        else:
            print("\nBook is already available in the library.")

    def display_status(self):
        print("\n------ Book Details ------")
        print("Title       :", self.title)
        print("Author      :", self.author)

        if self.available:
            print("Status      : Available")
            print("Borrower    : None")
        else:
            print("Status      : Issued")
            print("Borrower    :", self.borrower)


# User Input
title = input("Enter Book Title: ")
author = input("Enter Author Name: ")

# Create Object
book1 = LibraryBook(title, author)

# Display Initial Status
book1.display_status()

# Issue Book
borrower = input("\nEnter Borrower Name: ")
book1.issue_book(borrower)

# Display Status
book1.display_status()

# Return Book
book1.return_book()

# Display Final Status
book1.display_status()
