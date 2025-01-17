num = input('Enter any year : ')


if((float(num)%4 ==0 and float(num)%100 != 0 ) or float(num)%400 ==0):
    print('This Year {0} is Leap Year'.format(num))
else:
    print('The Year {0} is not Leap Year'.format(num))
    