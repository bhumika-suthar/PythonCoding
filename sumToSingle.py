num = str(input("Enter a number : "))
sum = 0
while True:
    sum = 0
    for n in num:
        sum += int(n)
    
    if(sum < 10):
            print(f"The final one digit sum will be : {sum}")
            break;
    else:
        print(f"Intermediate sum: {sum}")
        num = str(sum)
