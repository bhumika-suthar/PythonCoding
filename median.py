def sortArr(arr):
    length = len(arr)
    for i in range (length):
        for j in range (length-i-1):
            if(arr[j] > arr[j+1]):
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
    return arr

def median(arr1):
    arr = sortArr(arr1)
    length = int(len(arr))
    halfLen = int(len(arr)/2)
    if(length%2 != 0):
        print(f"The median in {arr} will be {arr[halfLen]}")
    else:
        med = (arr[halfLen-1] + arr[halfLen])/2
        print(f"The median in {arr} will be {med}")

arr = [3, 1, 2, 4, 5]
median(arr)
