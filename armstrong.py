inputVal = input('Enter any number : ')
num = int(inputVal)
ones = num%10
tens = (num%100 - ones)/10
hundreds = (num - num%100)/100
print('the ones {0} , tens {1} and hundreds {2}'.format(ones,tens,hundreds))

if( (ones**3 + tens**3 + hundreds**3) == num):
    print('This number {0} is Armstrong Number :'.format(num) )
else:
    print('This number {0} is not Armstrong Number :'.format(num) )
