list = [1, 2, 3, 4, 5, 6, 7, 8]

print("List Before swaping=", list)

    ## Aproach-3 ##


# get=(list[-1],list[0])  #packing 8 1
#
# list[0],list[-1] = get
#
# print("List After swaping=", list)

    ## Aproach-4 ##  *operand

# start,*middle,end = list

# list = [end,*middle,start]

# print("List After swaping=", list)


    ## Aproach-5 ## using pop()

# first = list.pop(0)
# last = list.pop(-1)
#
# list.insert(0,last)
# list.append(first)
#
# print("List After swaping=", list)
