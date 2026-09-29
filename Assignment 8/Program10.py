

# 10. Check Whether Year is Leap Year

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

year = int(input("Enter year: "))

if is_leap_year(year):
    print(f"{year} is a Leap year")
else:
    print(f"{year} is Not a leap year")

