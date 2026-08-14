m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
m4 = int(input("Enter marks of subject 4: "))
m5 = int(input("Enter marks of subject 5: "))
 
total = m1 + m2 + m3 + m4 + m5
percentage = total / 5
 
if (percentage >= 70):
    print(f"Percentage(%):{percentage} get Distinction.")
elif (percentage >= 60):
    print(f"Percentage(%):{percentage} get First Class.")
elif (percentage >= 50):
    print(f"Percentage(%):{percentage} get Second Class.")
elif (percentage >= 40):
    print(f"Percentage(%):{percentage} get Pass Class.")
else:
    print(f"Percentage(%):{percentage} get Fail.")

 
 