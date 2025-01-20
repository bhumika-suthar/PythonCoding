arr = [2,4,5,1,7,8,3,12,10, 0, 123]
small =arr[2]
large = arr[2]
for digit in arr:
    if(digit > large):
        large = digit
    if(digit < small):
        small = digit
print(f"Small: {small}")
print(f"Large: {large}")