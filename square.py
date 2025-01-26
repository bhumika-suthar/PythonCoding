num = int(input("Enter any number: "))
x = 1
for i in range(num):
    for j in range (num):
        print(f" {x} ", end="")
        x += 1
    print(f" ")