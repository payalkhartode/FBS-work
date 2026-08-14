

#     1
#    1 1
#   1 2 1
#  1 3 3 1

n = 1
for i in range(1, 5):

    for j in range(1 , i - 1):
        print(" ", end=" ")
    val = 1
    for j in range(i + 1):
        print(val, end=" ")
        val = val * (i - j) // (j + 1)
    print()
print()


