
### write a program to print list of odd number from given list.

L = [10, 15, 20, 25, 30, 35]
odd = []

for i in L:
    if i % 2 != 0:
        odd.append(i)

print(odd)