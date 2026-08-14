print("Q5. Type of Triangle")
s1 = float(input("Enter side 1: "))
s2 = float(input("Enter side 2: "))
s3 = float(input("Enter side 3: "))
 
if s1 == s2 == s3:
    print("Trangle is Equilateral Triangle.")
elif s1 == s2 or s2 == s3 or s1 == s3:
    print("Triangle is Isosceles Triangle.")
else:
    print("Triangle is Scalene Triangle.")

 