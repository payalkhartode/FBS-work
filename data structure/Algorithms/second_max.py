

lis = [10, 25, 5, 40, 30, 63, 98, 69]

max = lis[0]
sec_max = lis[0]

for i in lis:

    if (i > max):

         sec_max = max
         max = i

    elif (i > sec_max) and (i != max):

        sec_max = i

print(f'Second maximun value in given list is {sec_max}.')

