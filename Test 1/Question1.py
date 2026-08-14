
## Question 1 ) Write a program to calculate the area and perimeter for given figure.
 
length = float(input("Enter  the length: "))
breadth = float(input("Enter the breadth: "))
radius = float(input("Enter the radius: "))
 
pi = 3.14159
 
area = (length * breadth) + (0.5 * pi * radius * radius)
perimeter = (2 * length) + breadth + (pi * radius)
 
print("Area =", area)
print("Perimeter =", perimeter)
 
