num = int(input("Enter a number : "))
i = 1
factorial = 1
while (i < num+1):
    factorial *= i
    i += 1
print("{0}! is {1}".format(num, factorial))