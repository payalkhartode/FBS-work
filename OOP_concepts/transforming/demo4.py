
### write the program to add 10 into odd number of given list and print them.

li = [10, 2, 3, 4, 7, 11, 33]
new = []

for i in li:
    if i % 2 != 0:
        new.append(i + 10)

print(new)