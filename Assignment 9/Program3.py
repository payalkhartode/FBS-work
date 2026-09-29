
#3. Reverse a given number using recursive function

def reverse_number(num, rev=0):
    if num == 0:
        return rev
    digit = num % 10
    rev = rev * 10 + digit
    return reverse_number(num // 10, rev)

num = int(input("Enter a number: "))
print("Reverse of number =", reverse_number(num))
print()

