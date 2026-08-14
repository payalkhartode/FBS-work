

# 4. WAP to print Armstrong number within a given range.


start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

for n in range(start, end + 1):

    temp = n
    digits = len(str(n))
    sum = 0

    while (temp > 0):

        digit = temp % 10
        sum = sum + digit ** digits
        temp = temp // 10

    if (sum == n):

        print(n, end=" ")
        
print()
