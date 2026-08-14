days=int(input('Enter the number of days: '))
years=days//365
remaindays=days%365
weeks=remaindays//7
remaining_days=remaindays%7
print(f'years in given days is {years} years.')
print(f'weeks in given days is {weeks} weeks.')
print(f'remaining days after years and weeks is {remaining_days} days')