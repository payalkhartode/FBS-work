
cost_price = int(input("Enter the cost price of product: "))
selling_price = int(input("Enter the selling price of this product: "))
 
if (selling_price > cost_price):
    profit = selling_price - cost_price
    print(f"Profit is = {profit}.")
elif (cost_price > selling_price):
    loss = cost_price - selling_price
    print(f"Loss is = {loss}.")
else:
    print("There is No Profit and No Loss.")
