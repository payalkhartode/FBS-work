
#1 for memory optimization
#2 Genrating value according to the user
#3 Use yield keyword
#4 Maintain state(maintain stack frame) of function
#5 Iterate upcoming value using next from iterable

def generatevalues(n):
    for i in range(1,n+1):
        yield i

res = generatevalues(5)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))