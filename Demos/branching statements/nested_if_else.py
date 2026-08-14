gender=input('Enter the gender(f/m): ')
age=int(input('Enter the age: '))

if(gender=='f'):
    if(age>=18):
        print('Girl is eligibal for marriage.')
    else:
        print('Girl is not eligibal for marriage.')
else:
    if(age>=21):
        print('Boy is eligibal for the marriage.')
    else:
        print('Boy is not eligiable for the marriage.')