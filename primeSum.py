num1 = int(input('Enter start range : '))
num2 = int(input('Enter ending range : '))

arr = []
for num in range(num1, num2):
    i = 2
    sum = 0
    while i < float(num):
        if(float(num)%i ==0):
            sum += 1
            i += 1
        i += 1
    if(sum == 0):
        arr.append(num)
sum1 =0 
for num in arr:
    sum1 += num

print(f"The prime numbers in the range from {num1} to {num2} are {arr}")

print(f"The prime number sum in the range from {num1} to {num2} is {sum1}")
