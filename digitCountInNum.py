num = str(input("Enter a number : "))
number = int(input("Enter a number : "))
sum = 0

for n in num:
    if(int(n) == number):
        sum += 1
print(f"The digit {number} in {num} occured {sum} times")
