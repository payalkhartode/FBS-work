
cost_price = int(input("Enter cost price of book: "))
discount_percent = int(input("Enter discount percentage(%): "))
discount_amount = (cost_price * discount_percent) / 100
selling_price = (cost_price - discount_amount)
print(f"Discount amount is = {discount_amount}")
print(f"Selling price is = {selling_price}")



