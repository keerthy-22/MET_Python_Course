class Product:
    def __init__(self, product_id, product_name, price, quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def display_details(self):
        print("\n------ Product Details ------")
        print("Product ID   :", self.product_id)
        print("Product Name :", self.product_name)
        print("Price        : ₹", self.price)
        print("Quantity     :", self.quantity)

    def update_stock(self, new_quantity):
        self.quantity = new_quantity
        print("\nStock updated successfully.")

    def calculate_inventory_value(self):
        total_value = self.price * self.quantity
        print("Total Inventory Value: ₹", total_value)


# User Input
product_id = int(input("Enter Product ID: "))
product_name = input("Enter Product Name: ")
price = float(input("Enter Product Price: "))
quantity = int(input("Enter Quantity: "))

# Create Object
product1 = Product(product_id, product_name, price, quantity)

# Display Product Details
product1.display_details()

# Update Stock
new_quantity = int(input("\nEnter New Quantity: "))
product1.update_stock(new_quantity)

# Display Updated Details
product1.display_details()

# Calculate Inventory Value
product1.calculate_inventory_value()
