num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
i =1
common = 1
maxVal = max(num1,num2)
minVal = min(num1,num2)
if(maxVal%minVal == 0):
    print("The GCD of {0} and {1} is {2}".format(num1,num2,minVal))
else:
    while (i < max(num1,num2)+1):
    
        if(minVal%i == 0):
            if(maxVal%i == 0):
                common = i
        i += 1

    print("The GCD of {0} and {1} is {2}".format(num1,num2,common))
