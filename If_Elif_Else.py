#Product Invoice
pid=int(input("Enter your pid:"))
name=input("Enter your Name:")
price=float(input("Enter your price:"))
quantity=int(input("Enter your quantity:"))
print(f"PID={pid},NAME={name},PRICE={price}and QUANTITY={quantity}")
total=price*quantity
discount=0.0
if total<5000:
    discount=(total*15)/100
elif total>5000 and total<10000:
    discount=(total*21)/100
elif total>10000 and total<30000:
    discount=(total*31)/100
elif total>=30000:
    discount=(total*35)/100
else:
    print("Invalid data")
gst=(total*18)/100
final_bill=(total-discount)+gst
print(f"total={total}")
print(f"discount={discount}")
print(f"gST={gst} and FINAL_BILL={final_bill}")
#Electricity Bill
ConsumerId = int(input("Enter the ID: "))
ConsumerName = input("Enter the Name: ")
CurrentReading = int(input("Enter the Current Reading: "))
PreviousReading = int(input("Enter the Previous Reading: "))
units = CurrentReading - PreviousReading
if units <= 300:
    rate = 1.75
elif units <= 500:
    rate = 3.25
else:
    rate = 7.25
Total_Bill = units * rate
print("\n----- Electricity Bill -----")
print("Consumer ID :", ConsumerId)
print("Consumer Name :", ConsumerName)
print("Current Reading :", CurrentReading)
print("Previous Reading :", PreviousReading)
print("Units Consumed :", units)
print("Rate :", rate)
print("Total Bill :", Total_Bill)
#Employee Details
emp_no = int(input("Enter Employee No: "))
emp_name = input("Enter Employee Name: ")
salary = float(input("Enter Salary: "))
if salary <= 30000:
    ta = salary * 0.07
    da = salary * 0.09
    hra = salary * 0.11
    pf = salary * 0.15
elif salary <= 50000:
    ta = salary * 0.12
    da = salary * 0.13
    hra = salary * 0.17
    pf = salary * 0.22
else:
    ta = salary * 0.17
    da = salary * 0.19
    hra = salary * 0.21
    pf = salary * 0.25
gross_salary = salary + ta + da + hra
net_salary = gross_salary - pf
print("\nEmployee No :", emp_no)
print("Employee Name :", emp_name)
print("Salary :", salary)
print("TA :", ta)
print("DA :", da)
print("HRA :", hra)
print("PF :", pf)
print("Gross Salary :", gross_salary)
print("Net Salary :", net_salary)
