num = int(input("Enter a three-digit number: "))
original = num
digit1 = num // 100
digit2 = (num // 10) % 10
digit3 = num % 10
reversed_num = (digit3 * 100) + (digit2 * 10) + digit1
 
if (original == reversed_num):
    print(f'{original}is a Palindrome')
else:
    print(f"{original} is Not a Palindrome")

 