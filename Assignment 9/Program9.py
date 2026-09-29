
#9. Calculate m to the power n using recursion


def power(m, n):
    if n == 0:
        return 1
    else:
        return m * power(m, n - 1)

m = int(input("Enter base (m): "))
n = int(input("Enter power (n): "))
print(m, "^", n, "=", power(m, n))
print()
