basic = int(input("Enter basic salary of employee: "))
da = 0.10 * basic
ta = 0.12 * basic
hra = 0.15 * basic
total_salary = (basic + da + ta + hra)
print(f"DA is = {da}")
print(f"TA is = {ta}")
print(f"HRA is = {hra}")
print(f"Total Salary of employee is = {total_salary}")

