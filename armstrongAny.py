num = int(input('Enter any number : '))
order = len(str(num))
num1 = num
sum= 0
while num1 > 0:
    digit = num1%10
    sum += digit**order
    num1 //= 10
if( sum == num):
    print('This number {0} is Armstrong Number :'.format(num) )
else:
    print('This number {0} is not Armstrong Number :'.format(num) )
