#input

p=int(input("Enter the principle amount(p):"))
r=float(input("Enter the rate of interest(r): "))
t=int(input("Enter the time (t) in years: "))

#calculate simple interest

SI=(p*r*t)/100

#Display the Result

print(f'Simple Interest is {SI}')