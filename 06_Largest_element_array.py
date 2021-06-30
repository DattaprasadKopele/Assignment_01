'''Q.6 max no.of array'''


array = [11, 22, 33, 88, 44, 100, 50, 99]

max=array[0]

n=len(array)

for i in range(1,n):
    if array[i]>max:
        max=array[i]

print(max)



'''minimum no.of array'''

'''

min=array[0]

n=len(array)

for i in range(1,n):
    if array[i]<min:
        min=array[i]

print(min)

'''