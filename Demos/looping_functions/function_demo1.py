##1 pass: to neglate expected indented block error

for i in range(1,11):
    pass
    print(i)


##2 break: To terminate the flow of loop

for i in range(1, 10):
    if (i==3):
        break

    print(i)



##3 continue: used to skip the current iteration 

for i in range(1, 10):
    if (i==3):
        continue
    print(i)




##4 else

for i in range(1, 10):
    if (i==3):
        continue
    print(i)
else:
        print('block of else is exicute')






        