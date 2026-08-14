num = int(input("Enter a three-digit number: "))
digit1 = (num // 100)
digit2 = (num // 10) % 10
digit3 = (num % 10)
digit_sum = (digit1 + digit2 + digit3)
print(f"Sum of digits is = {digit_sum}")


