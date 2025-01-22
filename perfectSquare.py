def perfectSquare(num):
    x = int(num/2)
    n = 1
    for n in range(x+1) :
        if(n*n == num):
            print(f"this is true for {n}")
            return True
    return False

num = int(input("Enter a number : "))
if(perfectSquare(num)):
    print(f"The number {num} is the perfect square")
else:
    print(f"The number {num} is not perfect square")
