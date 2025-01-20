r1 = int(input('Enter starting range : '))
r2 = int(input('Enter ending range : '))
order = len(str(r2))

arr = []
for num in range(r1, r2):
    num1 = num
    sum= 0
    while num1 > 0:
        digit = num1%10
        sum += digit**order
        num1 //= 10
    if( sum == num):
        arr.append(num)
print(f"The Armstrong numbers in the range {r1} and {r2} are : {arr}" )
        

    