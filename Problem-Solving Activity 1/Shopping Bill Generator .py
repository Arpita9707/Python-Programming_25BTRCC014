customer_name = input("Enter customer name: ")
product1 = input("Enter name of product 1: ")
price1 = float(input("Enter price of product 1: ₹"))
product2 = input("Enter name of product 2: ")
price2 = float(input("Enter price of product 2: ₹"))
product3 = input("Enter name of product 3: ")
price3 = float(input("Enter price of product 3: ₹"))
total_amount = price1 + price2 + price3
if total_amount > 3000:
    discount = total_amount * 10 / 100
else:
    discount = 0
final_amount = total_amount - discount
print("\n========== SMART SHOPPING BILL ==========")
print(f"Customer Name : {customer_name}")
print("\nProduct Details:")
print(f"{product1} : ₹{price1:.2f}")
print(f"{product2} : ₹{price2:.2f}")
print(f"{product3} : ₹{price3:.2f}")
print(f"\nTotal Amount          : ₹{total_amount:.2f}")
print(f"Discount              : ₹{discount:.2f}")
print(f"Final Payable Amount  : ₹{final_amount:.2f}")
print("==========================================")