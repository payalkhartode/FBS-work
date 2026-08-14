

n = 5
 
for i in range(1, n + 1):
    # Spaces
    for j in range(n - i):
        print(" ", end=" ")
 
    if i == 1:
        print(1)
 
    elif i == n:
        for j in range(1, n + 1):
            print(j, end=" ")
        print()
 
    else:
        print(1, end=" ")
        for j in range(i - 2):
            print(" ", end=" ")
        print(i)
 
print()