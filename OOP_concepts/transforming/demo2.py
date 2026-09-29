
#### Write a program to print list of squarroot of each element of list .

li = [1, 4, 16, 49, 9]
newli = []

for i in li:
    newli.append(int(i ** 0.5))

print(newli)