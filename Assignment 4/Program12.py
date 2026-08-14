##12 WAP to check if given number is Armstrong number or not.


num = int(input("Enter the number: "))  
temp = num
digits = len(str(num))      ## number of digits present in given number.
sum = 0

while (temp > 0):
    digit = temp % 10             ## digit separation
    sum = sum + digit ** digits   ## separated digit power by number of digits of number(digits).
    temp = temp // 10             ## Remaining number
if (sum == num):
    print(f"{num} is an Armstrong Number.")
else:
    print(f"{num} is not an Armstrong Number.")
