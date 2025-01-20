def star(number, shape):
    shape = shape.lower()
    if shape == "pyramid":
        for i in range(number):
            print(' ' * (number - i - 1) + '*' * (2 * i + 1))
    elif shape == "square":
        for i in range(number):
            print("*" * number)
    elif shape == "triangle":
        for i in range(1, number + 1):
            print("*" * i)
    else:
        print("Incorrect Input")

star(5, "pyramid")

