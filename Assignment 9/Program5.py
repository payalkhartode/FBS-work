
#5. Factorial using recursion

def factorial_recursive(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial_recursive(num - 1)

num = int(input("Enter a number: "))
print("Factorial =", factorial_recursive(num))
print()
