
#1. Sum of series 1!+2!+3!+4!+.....+n! using recursive functions
#Note: two recursive functions - one for factorial, one for sum

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def sum_factorial_series(n):
    if n == 1:
        return factorial(1)
    else:
        return factorial(n) + sum_factorial_series(n - 1)

n = int(input("Enter n: "))
print("Sum of 1!+2!+3!+...+n! =", sum_factorial_series(n))
print()
