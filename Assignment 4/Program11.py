##11  WAP to check if given number is Strong Number.


num = int(input("Enter the number: "))
temp = num
sum = 0
while (temp > 0):
    digit = temp % 10           ## digit separate
    fact = 1

    for i in range(1, digit + 1):
        fact = fact * i
    sum = sum + fact
    temp = temp // 10          ## Remaining number
    
if (sum == num):
    print(f"{num} is a Strong Number.")          
else:
    print(f"{num} is not a Strong Number.")
