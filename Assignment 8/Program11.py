

# 11. Check Armstrong Number

def is_armstrong(num):
    original = num
    digits = len(str(num))
    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit ** digits
        num = num // 10

    if total == original:
        return True
    else:
        return False

num = int(input("Enter a number: "))

if is_armstrong(num):
    print(" Number is an Armstrong number")
else:
    print(" Number is Not an Armstrong number")
