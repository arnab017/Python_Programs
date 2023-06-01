
#^ Python Program to Print All Numbers in a Range Divisible by a Given Number

ll = int(input('Enter lower limit : '))
ul = int(input('Enter upper limit : '))
n = int(input('Enter the number to be divided by : '))
for i in range(ll, ul):
    if i%n==0:
        print(i)
        