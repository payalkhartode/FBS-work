##2 Enter number of students. For each, accept marks of 5 subjects,
 #calculate percentage. Display all percentages and average percentage.


num = int(input("Enter the number of students: "))
total_percentage = 0
for i in range(1, num + 1):
    print(f"Student {i}")
    m1 = float(input("Enter marks of subject 1: "))
    m2 = float(input("Enter marks of subject 2: "))
    m3 = float(input("Enter marks of subject 3: "))
    m4 = float(input("Enter marks of subject 4: "))
    m5 = float(input("Enter marks of subject 5: "))
    total = (m1 + m2 + m3 + m4 + m5)
    percentage = (total / 5)
    print(f"Percentage of student {i} = {percentage}")
    total_percentage = (total_percentage + percentage)

average_percentage = (total_percentage / num)
print(f"Average percentage of all students = {average_percentage}")


