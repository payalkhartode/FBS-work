
# 5. WAP to print prime numbers between 1 to 100.

for n in range(2, 101):

    value = True

    for i in range(2, n // 2 + 1):

        if (n % i == 0):
            value = False
            break

    if (value):

        print(n, end=" ")

print()





# 5. WAP to print prime numbers between 1 to 100 (using for-else).



for num in range(2, 101):

    for i in range(2, num):

        if (num % i == 0):

            break

    else:
        
        print(num, end=" ")