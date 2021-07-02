"""Python program to spplit the array and add the first part to the end"""


# def splitArr(arr, n, k):
#     for i in range(0, k):
#         x = arr[0]
#         for j in range(0, n - 1):
#             arr[j] = arr[j + 1]
#
#         arr[n - 1] = x
#
#

# arr = [12, 10, 5, 6, 52, 36, 40, 60]
# n = len(arr)
# position = 2
#
# splitArr(arr, n, position)
#
# for i in range(0, n):
#     print(arr[i], end=' ')


#### Method 2


def SplitAndAdd(A, length, rotation):
    # make a temporary array with double
    # the size and each index is initialized to 0
    tmp = [0 for i in range(length * 2)]

    # copy array element in to new array twice
    for i in range(length):
        tmp[i] = A[i]
        tmp[i + length] = A[i]

    for i in range(rotation,
                   rotation + length, 1):
        A[i - rotation] = tmp[i];


# Driver code
arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2
SplitAndAdd(arr, n, position);
for i in range(n):
    print(arr[i], end=" ")
print()











