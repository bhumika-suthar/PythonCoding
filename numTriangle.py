word = int(input('Enter the number of rows : '))


x = 0
j = 1
while(x <= word):
    i =0
    while (i < x):
            print(f" {j} ", end='')
            j += 1
            i += 1
    
    print("")
    x += 1
    