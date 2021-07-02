""" Count occurance of an element in list """



# def countn(list, n):
#     count = 0
#
#     for ele in list:
#         if (ele == n):
#             count = count+1
#     return count
#
# list = [10, 20, 10, 30, 20, 40, 10, 40, 50, 60, 80, 90, 80]
# n = int(input("Enter an element:"))
# print("{} has occurred {} times".format(n, countn(list, n)))
#



#### method-2

# def countX(lst, x):
#     return lst.count(x)
#
#
# lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
# x = 8
# print('{} has occurred {} times'.format(x, countX(lst, x)))


#### Method 3


from collections import Counter

## declaring the list
# l = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
#
# x = 3
# d = Counter(l)
# print('{} has occurred {} times'.format(x, d[x]))
#