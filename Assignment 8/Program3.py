
# 3. Sum of Series Using Functions


# a. 1 + 2 + 3 + 4 + ..... + n


def sum_series(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total

n = int(input("Enter n: "))

result = sum_series(n)

print("Sum =", result)


# b. 1! + 2! + 3! + 4! + ..... + n!


def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

def sum_factorial_series(n):
    total = 0

    for i in range(1, n + 1):
        total = total + factorial(i)

    return total

n = int(input("Enter n: "))

result = sum_factorial_series(n)

print("Sum of factorial series =", result)


# c. 1^1 + 2^2 + 3^3 + ..... + n^n


def power_series(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i ** i

    return total

n = int(input("Enter n: "))

result = power_series(n)

print("Sum =", result)

