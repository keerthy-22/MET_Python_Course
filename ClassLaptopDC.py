class Laptop:
    def __init__(self):
        self.brand = "Dell"
        self.model = "Inspiron 15"
        self.ram = "8 GB"
        self.storage = "512 GB SSD"

    def display_info(self):
        print("------ Laptop Details ------")
        print("Brand   :", self.brand)
        print("Model   :", self.model)
        print("RAM     :", self.ram)
        print("Storage :", self.storage)


# Create Object
laptop1 = Laptop()

# Display Default Information
laptop1.display_info()
