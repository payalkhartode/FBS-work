
#8. Check whether a number is prime or not using recursion

def check_prime(num, i=2):
    if num < 2:
        return False
    if i > num // 2:
        return True
    if num % i == 0:
        return False
    return check_prime(num, i + 1)

num = int(input("Enter a number: "))
if check_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
print()
