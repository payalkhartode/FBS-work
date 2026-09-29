
#2. Check if given number is Armstrong or not using recursive function


def sum_of_power_digits(num, total_digits, position=0):
    if num == 0:
        return 0
    digit = num % 10
    return (digit ** total_digits) + sum_of_power_digits(num // 10, total_digits, position + 1)

def count_digits(num):
    if num == 0:
        return 0
    return 1 + count_digits(num // 10)

num = int(input("Enter a number: "))
digits = count_digits(num)
total = sum_of_power_digits(num, digits)
if total == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
print()

