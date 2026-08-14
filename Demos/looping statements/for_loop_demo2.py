num1=int(input('Enter the number:'))
num2=int(input('Enter the number:'))

for number in range(num1,num2,+1):
    if(number % 2 != 0):
        print(number)