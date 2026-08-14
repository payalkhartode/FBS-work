num1=20
num2=10
str1='abc'
str2='xyz'

#1 + (Arithematic operator)
##Addition
print(num1+num2)
##Concatenation
print(str1+str2)

##print(num1+str1)

#2 -
##Subtrction
print(num1-num2)

#3 *
## multiplication
print(num1*num2)

#4 /
##division
print(5/2)

#5 //
##floor division
print(5//2)

#6 %
##modolus
print(5/2)

#7 **
##Exponential
print(4**2)


##2 Assignment operators

#1 =
x=10

#2 +=
x+=5

#3 -=
x-=3

#4 *=
x*=5

#5 /=
x/=2

#6 //=
x//=2

#7 %=
x%=2

#8 **=
x**=4
print(x) 


##3 comparission operators

x=10
y=20
z=10

#1 ==
print(x==y)

#2 !=
print(y!=x)

#3 >
print(y>x)

#4 >=
print(x>=y)

#5 <
print(x<y)

#6 <=
print(y<=20)


### logical operators

#1 and
print(True and True)

#2 or 
print(False or False)

#3 not
print(not False)

### membership operators

#1 in
print('first' in 'Firstbit solution')

# not in
print('first' not in 'Firstbit solution')


### identity operators
x=10
y=10
z=20

li1=[10,20]
li2=[10,20]

print(id(x))
print(id(y))

print(x is y)

print(x is z)

print(id(li1))
print(id(li2))

print(li1 is li2)