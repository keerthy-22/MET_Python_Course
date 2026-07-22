class Laptop:
    def __init__(self, brand, processor, ram, price):
        self.brand = brand
        self.processor = processor
        self.ram = ram
        self.price = price

    def display_details(self):
        print("\n------ Laptop Details ------")
        print("Brand      :", self.brand)
        print("Processor  :", self.processor)
        print("RAM        :", self.ram, "GB")
        print("Price      : ₹", self.price)


# User Input
brand = input("Enter Laptop Brand: ")
processor = input("Enter Processor: ")
ram = int(input("Enter RAM (GB): "))
price = float(input("Enter Price: "))

# Create Object
laptop1 = Laptop(brand, processor, ram, price)

# Display Details
laptop1.display_details()
