
### Write a program to print the lable to given list number are even or odd.

li = [7, 2, 11, 19, 10, 26]
newli = []

for i in li:
    if i % 2 == 0:
        newli.append("even")
    else:
        newli.append("odd")

print(newli)