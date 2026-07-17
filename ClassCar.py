class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print("Car Information")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Manufacturing Year:", self.year)

    def check_age(self):
        current_year = 2026
        if current_year - self.year > 10:
            print("The car is older than 10 years.")
        else:
            print("The car is not older than 10 years.")


# Create object
car1 = Car("Toyota", "Innova", 2012)

# Call methods
car1.display_info()
car1.check_age()
