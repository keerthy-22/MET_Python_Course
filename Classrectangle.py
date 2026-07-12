class Rectangle:
    # Constructor
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to calculate area
    def calculate_area(self):
        return self.length * self.width

    # Method to calculate perimeter
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    # Method to display rectangle details
    def display_details(self):
        print("Length:", self.length)
        print("Width:", self.width)
        print("Area:", self.calculate_area())
        print("Perimeter:", self.calculate_perimeter())


# Create an object
rect = Rectangle(10, 5)

# Display details
rect.display_details()
