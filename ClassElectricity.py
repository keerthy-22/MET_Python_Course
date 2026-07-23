class ElectricityBill:
    def __init__(self, customer_name, units_consumed, cost_per_unit):
        self.customer_name = customer_name
        self.units_consumed = units_consumed
        self.cost_per_unit = cost_per_unit

    def calculate_bill(self):
        bill = self.units_consumed * self.cost_per_unit

        # Apply surcharge if bill exceeds ₹5000
        if bill > 5000:
            surcharge = bill * 0.10   # 10% surcharge
            bill += surcharge
            print("Surcharge Applied: ₹", surcharge)
        else:
            print("No Surcharge Applied.")

        return bill

    def display_details(self):
        print("\n------ Electricity Bill ------")
        print("Customer Name :", self.customer_name)
        print("Units Consumed:", self.units_consumed)
        print("Cost Per Unit : ₹", self.cost_per_unit)
        print("Total Bill    : ₹", self.calculate_bill())


# User Input
customer_name = input("Enter Customer Name: ")
units_consumed = int(input("Enter Units Consumed: "))
cost_per_unit = float(input("Enter Cost Per Unit: "))

# Create Object
bill1 = ElectricityBill(customer_name, units_consumed, cost_per_unit)

# Display Bill Details
bill1.display_details()
