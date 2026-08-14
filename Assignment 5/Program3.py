
# 3. Accept no. of passengers, per ticket cost, and age of each passenger.
#    Calculate total amount:
#    a. Below 12 = 30% discount
#    b. Above 59 = 50% discount
#    c. Others pay full


num = int(input("Enter the number  of passengers: "))
cost = float(input("Enter the cost per ticket: "))
total_amount = 0
for i in range(1, num + 1):

    age = int(input("Enter an age of passenger " + str(i) + ": "))
    if (age < 12):

        amount = cost - (cost * 30 / 100)

    elif (age > 59):

        amount = cost - (cost * 50 / 100)

    else:

        amount = cost

    total_amount = total_amount + amount
print("Total amount to be paid  is = ", total_amount)

