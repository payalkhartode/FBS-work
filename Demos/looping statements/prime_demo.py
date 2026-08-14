

num=int(input('Enter the number:'))

for i in range(2,num):
    print(i)
    if(num % i == 0):
        print(f'{num} is not a Prime number.')
        break
else:
    print(f'{num} is Prime number.')