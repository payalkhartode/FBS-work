num=int(input('Enter the number: '))
if(num<=0):
    print('Number is less than or equal to the zero.')
elif(num<=50):
    print(f'{num} number is between 1 to 50 .')
elif(num<=100):
    print(f'{num} Number is between 51 to 100.')
elif(num<=150): 
    print(f'{num} Number is between 101 to 150.')
elif(num<=250):
    print(f'{num} Number is between to 151 to 250.')
else:
    print(f'{num} Number is greater than 250.')