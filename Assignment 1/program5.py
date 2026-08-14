p=int(input("Enter the principle amount(p):"))
r=float(input("Enter the rate of interest(r): "))
t=int(input("Enter the time (t) in years: "))

A=p*(1+r)/100 **t

CI=A-p

print(f'The compond interest is {CI}')

