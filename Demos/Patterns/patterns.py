## Pattern 1

for i in range(1 ,6):
    for j in range(1, 6):
        print('*',end='')
    print()

## Pattern 2

for i in range(1 ,6):
    for j in range(1, 6):
        print(i,end='')
    print()

## Pattern 3

for i in range(1,6):
  for j in range(1, i + 1):
    print('*',end='')
  print()

## Pattern 4

for i in range(1, 6):
  for j in range(1, 7-i):
    print('*',end='')
  print()

## Pattern 5

for i in range(1 , 6):
    for j in range(i , 6):
      print(j,end='')
    print()

## Pattern 6

for i in range(1 , 6):
  for j in range(5, i-1, -1):
    print(j,end='')
  print()

## Pattern 7

for i in range(1,6):
  for j in range(6-i, 6):
    print(j,end='')
  print()

## Pattern 8

for i in range(1, 6):
  for j in range(1, 6):
    if (i % 2 == 0):
      print('$',end='')
    else:
      print('*',end='')
  print() 

## Pattern 9

for i in range(1, 6):
  for j in range(1, 6):
    if((i==1) or (i==5) or (j==1) or (j==5)):
      print('*',end='')
    else:
      print(' ',end='')
  print()

## Pattern 10

for i in range(1, 6):
  for j in range(1, 6):
    if ((i==1) or (j==1) or (i+j==6)):
      print('*',end='')
    else:
      print(' ',end='')
  print()

  ## Pattern 11

for i in range(65, 69):
    for j in range(1, 5):
      print(chr(i),end='')
    print()

## Pattern 12

for i in range(1, 5):
  for j in range(65, 69):
    print(chr(j),end='')
  print()

## Pattern 13

count=1
for i in range(1,5):
  for j in range(1,4):
    print(count,end='')
    count += 1
  print()

## Pattern 14

for i in range(1, 6):
  for j in range(1, i):
    print(' ',end='')
  
  for j in range(1, 7-i):
    print('*',end='')

  print()  



## Pattern 15

for i in range(1, 6):
  for j in range(1, 6-i):
    print(' ',end='')

  for j in range(1, i+1):
    print('*',end='')

  for j in range(1, i):
    print('*',end='')

  print()



## Pattern 16

for i in range(1, 6):
  for j in range(1, 6-i):
    print(' ',end='')

  for j in range(1, i * 2):
    print(j,end='')
  print()



## Pattern 17

for i in range(1, 6):
  for j in range(1, 6-i):
    print(' ',end='')
  
  for j in range(1, i+1):
    print('*  ',end='')

  print()  


## Pattern 18

for i in range(1, 6):
  for j in range(1, 6 - i):
    print(' ',end='')

  for j in range(i, i + 1):
    print('*',end='')

  print()



## Pattern 19


for i in range(1, 6):
  for j in range(1, 6-i):
    print(' ',end='')

  for j in range(1, i * 2):
    print(j,end='')
  print()


## Pattern 20


k=7
for i in range(1, 6):
  for j in range(1, i+1):
    print('*',end='')

  for j in range(1, k+1):
    print(' ',end='')

  k-=2
  for j in range(1, i+1):
    if (i!=5) or (j!=5):
      print('*',end='')

  print()


## Pattern 21

for i in range(1, 6):
  k=1
  for j in range(1, 6-i):
    print(' ',end='')

  for j in range(1, i+1):
    print(k,end='')
    k+=1

  k-=2

  for j in range(i-1, 0):
    print(k,end='')
    k-=1
        
  print()     


## Pattern 22

for i in range(1, 6):
  for j in range(6-i, 0, -1):
    if(i==1) or (j==1) or (i+j==6):
      print(j,end='')
    else:
      print(' ',end='')

  print()


## Pattern 23

for i in range(1, 6):
  for j in range(1,i+1):
    print(' ', end='')
  
  for j in range(1, 7-1):
    print('*', end='')

  print()


## 23

for i in range(1, 6):
  for j in range(1, i+1):
    print(' ',end='')

  for j in range(1, 7-i):
    print(chr(64 + i), end='')

  print()