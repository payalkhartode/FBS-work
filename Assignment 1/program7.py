
# Taking input from user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Step 1: Calculate discriminant

d = b*b - 4*a*c

# Step 2: Check the nature of roots

if d > 0:
    root1 = (-b + d**0.5) / (2*a)
    root2 = (-b - d**0.5) / (2*a)
    print("Root 1 =", root1)
    print("Root 2 =", root2)

elif d == 0:
    root1 = -b / (2*a)
    print("Root =", root1)

else:
    print("No real roots (discriminant is negative)")