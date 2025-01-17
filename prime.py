num = input('Enter a number : ')
i = 2
sum = 0
while i < float(num):
    if(float(num)%i ==0):
        sum += 1
        i += 1
    i += 1
if(sum == 0):
    print('The number {0} is prime'.format(num))
else:
    print('The number {0} is not prime'.format(num))
    