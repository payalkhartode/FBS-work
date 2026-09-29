
#10. Reverse a number using recursion


def reverse_num(num, rev=0):
    if num == 0:
        return rev
    digit = num % 10
    rev = rev * 10 + digit
    return reverse_num(num // 10, rev)

num = int(input("Enter a number: "))
print("Reverse of number =", reverse_num(num))
