num = int(input("ENter any number : "))
sum = 0
for n in range(1,num):
    if(num%n ==0):
        sum += n
if(sum == num):
    print(f"The number {num} is Perfect Number")
else:
    print(f"The number {num} is not Perfect Number")
