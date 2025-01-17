num = int(input("Enter how long you want the sequence:" ))
pre2 = 0
pre1 = 1
current = 0
i = 0
while (i <= num):
    print(current)
    current = pre2 + pre1
    pre1 = pre2
    pre2 = current
    i += 1

