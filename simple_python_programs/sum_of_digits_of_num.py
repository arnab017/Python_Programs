
#^ Python Program to Find Sum of Digits of a Number

n = int(input('Enter a Number : '))
summ = 0
while n > 0:
    rem = n%10
    summ = summ+rem
    n = n//10
print('Sum of digits of the number is',summ)
    

