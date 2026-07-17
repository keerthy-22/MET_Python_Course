import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

    def display_details(self):
        print("\n------ Circle Details ------")
        print("Radius        :", self.radius)
        print("Area          :", round(self.calculate_area(), 2))
        print("Circumference :", round(self.calculate_circumference(), 2))


# User Input
radius = float(input("Enter the radius of the circle: "))

# Create Object
circle1 = Circle(radius)

# Display Details
circle1.display_details()
