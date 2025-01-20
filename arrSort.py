arr = [2,4,5,1,7,8,3,12,10, 0, 123]
arr1 = [2,4,5,1,7,8,3,12,10, 0, 123]
length = len(arr)
for i in range (length):
    for j in range (length-i-1):
        if(arr[j] > arr[j+1]):
            arr[j] , arr[j+1] = arr[j+1] , arr[j]
print(f"The actual array is {arr1}")
print(f"The sorted array is {arr}")

