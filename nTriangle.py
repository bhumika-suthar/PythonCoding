def sumOfRange(r):
    sum = 0
    for n in range(r+1):
        sum += n
    print(f"The {r}th triangle number is {sum}")

num = int(input("Enter a Number : "))
sumOfRange(num)