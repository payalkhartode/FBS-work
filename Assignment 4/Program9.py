##9 WAP to print all numbers in a range divisible by a given number.


start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
num = int(input("Enter the divisor: "))

for i in range(start, end + 1):
    if (i % num == 0):
        print(i)


