

def BinarySearch(li, searchele):

    beg = 0
    end = len(lis)-1

    while(beg <= end):

        mid = ( beg + end )// 2

        if ( searchele == lis[mid]) :

            return mid

        elif ( searchele < lis[mid]) :
            end = mid - 1

        elif ( searchele > lis[mid]) :
            beg = mid + 1

    else:
        return -1


lis = [10,40,55,99,56,78,98,89,11]
searchele = int(input('Enter an element to find : '))
result = BinarySearch(lis, searchele)

if(result != -1):
    print(f'{searchele} is present at index {result}.')

else:
    print('Element is not found.')        


        