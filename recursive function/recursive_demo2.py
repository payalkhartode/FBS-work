

def digsep(num):
    if(num == 0):
        return
    dig = num % 10
    print(dig)
    digsep(num // 10)

no = int(input('Enter the number : '))
digsep(no)