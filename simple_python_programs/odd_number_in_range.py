
#^ Python Program to Print All Odd Numbers in a Range

ll = int(input('Enter lower limit : '))
ul = int(input('Enter upper limit : '))
for i in range(ll,ul+1):
    if i%2==1:
        print(i)

