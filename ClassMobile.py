class MobilePhone:
    def __init__(self, brand, ram, storage, price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.price = price

    def display_specs(self):
        print("\n------ Mobile Phone Details ------")
        print("Brand   :", self.brand)
        print("RAM     :", self.ram, "GB")
        print("Storage :", self.storage, "GB")
        print("Price   : ₹", self.price)

    def check_premium(self):
        premium_price = 50000

        if self.price > premium_price:
            print("This is a Premium Phone.")
        else:
            print("This is not a Premium Phone.")


# User Input
brand = input("Enter Brand Name: ")
ram = int(input("Enter RAM (GB): "))
storage = int(input("Enter Storage (GB): "))
price = float(input("Enter Price: "))

# Create Object
phone1 = MobilePhone(brand, ram, storage, price)

# Display Specifications
phone1.display_specs()

# Check Premium Status
phone1.check_premium()
