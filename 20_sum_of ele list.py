'''Sum of an element of list'''

    #### Approach 1

# list = [10, 20, 30, 40]
#
# print(sum(list))


#### Approach 2

# list = [10, 20, 30, 40]
#
# list2 =list[0]+list[1]+list[2]+list[3]
#
# print(list2)



#### Approach 3

# list = [10, 20, 30, 40]
#
# output = list[0]
# i=1
# ln=len(list)
#
# for ele in list:
#     if i<ln:
#         output= (output + list[i])
#     i = i + 1
# print(output)


#### Approach 4  -- for loop

# total = 0
#
# list1 = [11, 5, 17, 18, 23]

#for ele in range(0, len(list1)):

# 	total = total + list1[ele]
#
# print("Sum of all elements in given list: ", total)
#
# #### Approach 5  -- while loop

# total=0
# i=0
#
# list = [10, 20, 30, 40]
#
# while(i<len(list)):
#     total = total + list[i]
#     i+=1
#
# print("sum of all element in given list: ", total)


#### Approach 6  -- function

# list1 = [11, 5, 17, 18, 23]
#
# def sumOfList(list, size):
#     if (size == 0):
#         return 0
#     else:
#         return list[size - 1] + sumOfList(list, size - 1)
#
# total = sumOfList(list1, len(list1))
#
# print("Sum of all elements in given list: ", total)