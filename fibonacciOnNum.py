num = int(input("Enter the position of sequence:" ))
pre2 = 0
pre1 = 1
current = 0
i = 0
arr = []
while (i <= num):
    arr.append(current)
    current = pre2 + pre1
    pre1 = pre2
    pre2 = current
    i += 1

print(f"The number at location {num} is {arr[len(arr)-1]} ")



