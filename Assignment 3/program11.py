ticket_amount = int(input("Enter per person ticket amount: "))
total_amount = 0
 
for i in range(1, 6):
    age = int(input(f"Enter age of person {i}: "))
    if (age < 12):
        price = ticket_amount * 0.70          # 30% discount
        print(f"Person {i} (Child): Rs.{price}")
    elif (age > 59):
        price = ticket_amount * 0.50          # 50% discount
        print(f"Person {i} (Senior Citizen): Rs.{price}")
    else:
        price = ticket_amount                 # full payment
        print(f"Person {i} (Adult): Rs.{price}")
    total_amount += price
 
print(f"Total ticket amount for all 5 people = {total_amount}.")

