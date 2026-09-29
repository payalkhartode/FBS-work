

# 6. Fibonacci Series Using Function
# Series: 1 1 2 3 5 8 ...

def fibonacci(n):
    a = 1
    b = 1

    for i in range(n):
        print(a, end=" ")

        c = a + b
        a = b
        b = c

n = int(input("Enter number of terms: "))

fibonacci(n)
