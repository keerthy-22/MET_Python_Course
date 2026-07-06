products = {}

n = int(input("Enter number of products: "))

discount = 0

for i in range(n):
    name = input("Enter Product Name: ")
    price = int(input("Enter Price: "))
    products[name] = price

print("\nProducts")
print(products)

print("\nProduct Names")
for name in products.keys():
    print(name)

print("\nPrices")
for price in products.values():
    print(price)

name = input("\nEnter Product Name: ")

if name in products:
    price = products[name]
    print("Price =", price)

    quantity = int(input("Enter Quantity: "))

    total = price * quantity

    gst = total * 18 / 100
    final_bill = (total - discount) + gst

    print("TOTAL =", total)
    print("DISCOUNT =", discount)
    print("GST =", gst)
    print("FINAL BILL =", final_bill)

else:
    print("Product Not Found")
