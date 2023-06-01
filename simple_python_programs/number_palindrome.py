
#^ Python Program to Check if a Number is a Palindrome

n = int(input('Enter a number: '))
if n>0:
    num = n
    summ = 0
    while num>0:
        rem = num%10
        summ = summ*10+rem
        num = num//10
    if summ == n:
        print(n,'is palindrome')
    else:
        print(n,'is not palindrome')
else:
    print('Invalid input')
    