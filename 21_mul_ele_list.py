''' pp multiplication of all ele in list'''

# list = [10, 5, 2, 40]
# mul = 1
#
# for ele in range(0, len(list)):
#
# 	mul = mul * list[ele]
#
# print("multiplication of all elements in given list: ", mul)



###### Approach 2

# mul=1
# i=0
#
# list = [10, 20, 3, 4]
#
# while(i<len(list)):
#     mul = mul * list[i]
#     i+=1
#
# print("multiplication of all element in given list: ", mul)

####### Approach 3

# list = [10, 20, 3, 4]
#
# def mulOfList(list, size):
#     if (size == 0):
#         return 1
#     else:
#         return list[size - 1] * mulOfList(list, size - 1)
#
# mul = mulOfList(list, len(list))
#
# print("multiplication of all elements in given list: ", mul)


##### AppRoach 4

# list1 = [1, 2, 3]
#
# def multiplyList(myList):
#     result = 1
    ## mul = 1
    # for x in myList:
    #     result = result * x
       # # mul = mul * x
    #
    # return result
    # return mul
#
#
# print(multiplyList(list1))



#### Approach 5

# from functools import reduce
#
# list1 = [1, 2, 3]
# list2 = [3, 2, 4]
#
# result1 = reduce((lambda x, y: x * y), list1)
# result2 = reduce((lambda x, y: x * y), list2)
# print(result1)
# print(result2)


#### Approach 6

# import math
#
# list1 = [1, 2, 3]
# list2 = [3, 2, 4]
#
# result1 = math.prod(list1)
# result2 = math.prod(list2)
# print(result1)
# print(result2)

