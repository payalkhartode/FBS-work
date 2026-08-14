

# 6. WAP to print first n prime numbers.


n = int(input("Enter the number: "))   ## how many prime numbers you want print from 2.

count = 0
num = 2

while (count < n):

    i = 2
    
    while (i < num):

        if (num % i == 0):

            break

        i = i + 1

    else:

        print(num, end=" ")
        count = count + 1
    num = num + 1