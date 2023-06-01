
#^ Python Program to Find Numbers which are Divisible by 7 and Multiple of 5 in a Given Range


ll = int(input('Enter lower limit : '))
ul = int(input('Enter upper limit : '))
for i in range(ll, ul+1):
    if i%7==0 and i%5==0:
        print(i)