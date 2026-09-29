def Pallindrome(str):
    rev_str = ''
    for char in str :
        rev_str = char + rev_str
        # print(ver_str)

    if ( str == rev_str):
        print('The string is Pallindrome.')
    else:
        print('The string is not Pallindrome')

str = input('Enter the String :')
Pallindrome(str)





