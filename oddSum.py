r1 = int(input('Enter starting range : '))
r2 = int(input('Enter ending range : '))
sum = 0
for n in range(r1,r2+1):
    if (n%2 != 0):
        sum += n
print(f"The sum of odd numbers from range {r1} to {r2} is {sum}")