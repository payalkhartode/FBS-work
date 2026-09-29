

def printNum(start, end):

    if (start == end + 1):
        return

    print(start)
    printNum (start + 1,end)

start = int(input('Enter the starting value :'))
end = int(input('enter the ending value :' ))
printNum(start,end)
