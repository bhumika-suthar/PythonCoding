def factorial(num):
    i =1
    fac = 1
    while(i <= num):
        fac *= i
        i += 1
    print(f" the factorial is {fac}")
    return fac

inputNum = int(input("Enter any number : "))
number = factorial(inputNum)
sum = 0
while number > 0:
    digit = number%10
    sum += digit
    number //= 10
    
print(f"The sum of factorial of {inputNum} will be {sum}")
