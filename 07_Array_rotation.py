'''Q.7 Rotation of array'''

'''

arr = [11, 22, 33, 55, 44, 66, 88, 77, 99, 200, 100]

shift = 2

for i in range(0, shift):
    temp = arr[0]

    for j in range(0, len(arr)-1):
        arr[j] = arr[j+1]
    arr[len(arr)-1] = temp

for i in range(0, len(arr)):
    print(arr[i])

'''



'''

arr = [11, 22, 33, 55, 44, 66, 88, 77, 99, 200, 100]

shift = 2

def printarr(arr):
    for i in range(0, len(arr)):
    print(arr[i], end=' ')

def leftRotation(arr, shift)
    for i in range(0, shift):
        temp = arr[0]

        for j in range(0, len(arr)-1):
            arr[j] = arr[j+1]

    arr[len(arr)-1] = temp
    return arr

print("array before rotation")

'''