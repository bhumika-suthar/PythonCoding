num = int(input('Enter any number : '))
order = len(str(num))
num1 = num
sum= 0
while num1 > 0:
    digit = num1%10
    sum += digit
    num1 //= 10
print("the sum of {0} is {1}".format(num, sum))