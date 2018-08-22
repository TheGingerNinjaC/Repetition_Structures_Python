'''
Author: Chane van der Berg
Date: 22/04/2018

Practical based on repetition structures.
'''
# Question 1
# Display all values from 1 to n.

n = int(input("Enter the number of values to display: "))
i=1
while i<=n:
    print(i)
    i+=1

print()

# Question 2
# Receive range of real numbers and calculate the sum.
# Ask values until negative value is entered.

sum=0
flag=0
i=1

while not flag:
    val = float(input("Enter value number " + str(i) + ":"))
    i+=1
    if val < 0:
        flag=1
    else:
        sum+=val

print("The sum of",i-1,"values =",sum)

print()

# Question 3
# Convert any decimal integer to another number system
# with a different base number

val = int(input("Enter decimal number to convert to base: "))
base = int(input("Enter base for conversion: "))

a = ''
b = val

while b > 0:
    a = str(b%base) + a
    b //= base

if a=='10':
    print('A')
if a=='11':
    print('B')
if a=='12':
    print('C')
if a=='13':
    print('D')
if a=='14':
    print('E')
if a=='15':
    print('F')


print("Base",base,"value of",val,"=",a)
