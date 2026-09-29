

def linearSearch(lis, searchele):

    for ind in range(0, len(lis)):

        if (searchele == lis[ind]):

            return ind

    else:

        return -1


lis = [10,40,55,99,56,78,98,89,11]
ele = int(input('Enter an element to find : '))
result = linearSearch(lis, ele)

if(result != -1):
    print(f'{ele} is present at index {result}.')

else:
    print('Element is not found.')        