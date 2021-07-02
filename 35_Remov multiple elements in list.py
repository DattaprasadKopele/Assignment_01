''' Remove multiple elements from a list'''


#### Approach 1

# list =[10, 25, 20, 15, 22, 14,35, 55]
#
# for item in list:
#     if item%2 == 0:
#         list.remove(item)
#
# print(list)
#

##### Approach 2

# list =[10, 25, 20, 15, 22, 14, 35, 57, 88]
#
# for item in len(list):
#     if list[item] %2 != 0:
#         list.remove(item)
# print(list)



##### Approach 3

# list =[10, 25, 21, 15, 22, 14, 35, 57, 88]
# i=0;le=len(list)
# while i<le:
# item=list[i]
# if item %2 != 0:
# list.remove(item)
# else:
# i+=1
# print(list)


##########################

# list =[10, 25, 20, 15, 22, 14,35, 55]
#
# for item in list:
#     if item%2 != 0:
#         list.remove(item)
#
# print(list)

#################


# list1 = [11, 5, 17, 18, 23, 50]

   ## will create a new list,
    ## excluding all even numbers
# list1 = [elem for elem in list1 if elem % 2 != 0]
#
# print(*list1)
###############


# list1 = [11, 5, 17, 18, 23, 50]

   #### removes elements from index 1 to 4
###### i.e. 5, 17, 18, 23 will be deleted

# del list1[1:5]
#
# print(*list1)



###################

# list1 = [11, 5, 17, 18, 23, 50]

   ###### items to be removed
unwanted_num = {11, 5}

# list1 = [ele for ele in list1 if ele not in unwanted_num]

   ##### printing modified list
# print("New list after removing unwanted numbers: ", list1)



###############

  #### Python program to remove multiple
  #### elements from a list

 #### creating a list
# list1 = [11, 5, 17, 18, 23, 50]
#
  ##### given index of elements
  ##### removes 11, 18, 23
# unwanted = [0, 3, 4]
#
# for ele in sorted(unwanted, reverse = True):
# 	del list1[ele]

  ##### printing modified list
# print (*list1)
