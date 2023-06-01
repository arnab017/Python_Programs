
#^ Python Program to Print All Integers that Aren’t Divisible by Either 2 or 3

ll = int(input('Enter lower limit : '))
ul = int(input('Enter upper limit : '))
for i in range(ll,ul+1):
    if i%2==1 and i%3==1:
        print(i)
        
