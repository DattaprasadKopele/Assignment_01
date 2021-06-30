# arr = [11, 22, 33, 44, 55, 66, 77, 88]
#
# print(arr[::-1])


'''2'''

# arr.reverse()
# print(arr)

'''3'''

# arr2=[]
# for i in(7,0,-1):
#     arr2.append(arr[i])
# arr = arr2
# print(arr)

'''4'''
arr = [1, 2, 3, 4, 5, 6, 7, 8]

def reverse(a):
    start = 0        # Point to first element
    end = len(a)-1   # Point to last element

    while start < end:   #Swap element
        a[start], a[end] = a[end], a[start]
        start = start+1
        end = end-1

        print(a)

# arr = [1, 2, 3, 4, 5, 6, 7, 8]

reverse(arr)
