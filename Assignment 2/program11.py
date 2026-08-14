amount = int(input("Enter the amount: "))

note_500=amount//500
amount=amount%500

note_200=amount//200
amount=amount%200

note_100=amount//100
amount=amount%100

note_50=amount//50
amount=amount%50

note_20=amount//20
amount=amount%20

note_10=amount//10
amount=amount%10

note_5=amount//5
amount=amount%5

note_2=amount//2
amount=amount%2

note_1=amount//1
amount=amount%1

print(f"note of 500 = {note_500}, note of 200 is = {note_200}, note of 100 is = {note_100}, note of 50 is = {note_50}, note of 20 is = {note_20}, note of 10 is = {note_10}, note of 5 is = {note_5}, note of 2 is = {note_2} and note of 1 is = {note_1}.")


