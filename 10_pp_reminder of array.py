""" PP for find remind of array multiplication divided by n """


def findremainder(arr, lens, n):
    mul = 1

    # find the individual
    # remainder and
    # multiple with mul.
    for i in range(lens):
        mul = (mul * (arr[i] % n)) % n

    return mul % n

arr = [100, 10, 5, 25, 35, 14]
lens = len(arr)
n = 11
print(findremainder(arr, lens, n))