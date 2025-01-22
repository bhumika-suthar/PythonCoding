def power(base, expo):
    output = 1
    i = 0
    while i < expo:
        output *= base
        i += 1 
    print(f"The {expo} power of {base} is {output}")

baseVal = int(input("Enter base value:  "))
expoVal = int(input("ENter the Exponent value :  "))
power(baseVal, expoVal)