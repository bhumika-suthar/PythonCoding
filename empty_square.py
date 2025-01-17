word = int(input('Enter the number of rows : '))

i =0
x = 0
while(x < word):
    i = 0
    while (i < word):
        if(x == 0 or x == word -1):
            print(" * ", end='')
            i += 1
        elif(i == 0 ):
            print(" * ", end='')
            i += 1
        elif(i == word-1 ):
            print(" * ", end='')
            i += 1
        else:
            print("   ", end='')
            i += 1
    
    print("")
    x += 1
    