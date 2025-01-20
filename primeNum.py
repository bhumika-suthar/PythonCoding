
num2 = int(input('Enter ending range : '))

arr = []
for num in range(1, num2):
    i = 2
    sum = 0
    while i < float(num):
        if(float(num)%i ==0):
            sum += 1
            i += 1
        i += 1
    if(sum == 0):
        arr.append(num)
print(f"The prime numbers in the range from 1 to {num2} are {arr}")   