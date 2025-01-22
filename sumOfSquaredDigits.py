num = int(input("Enter the number: "))

num1 = num
sum = 0
while num > 0:
    digit = num%10
    sum += digit*digit
    num //= 10
print(f"The sum of squares of the number {num1} is {sum}")