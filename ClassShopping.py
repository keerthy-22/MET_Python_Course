class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

    def display_item(self):
        print("\nItem Name :", self.name)
        print("Price     : ₹", self.price)
        print("Quantity  :", self.quantity)
        print("Total     : ₹", self.total_price())


# Create an empty list
cart = []

# Get number of items
n = int(input("Enter number of items: "))

# Input item details
for i in range(n):
    print(f"\nEnter details for Item {i + 1}")
    name = input("Item Name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    item = Item(name, price, quantity)
    cart.append(item)

# Display Cart
print("\n========== Shopping Cart ==========")
total_bill = 0

for item in cart:
    item.display_item()
    total_bill += item.total_price()

print("\n===============================")
print("Total Bill: ₹", total_bill)
print("===============================")
