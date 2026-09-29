


# 5. Sum of All Prime Numbers Between 1 to n

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def sum_prime(n):
    total = 0

    for i in range(1, n + 1):
        if is_prime(i):
            total = total + i

    return total

n = int(input("Enter number: "))

result = sum_prime(n)

print("Sum of prime numbers =", result)

