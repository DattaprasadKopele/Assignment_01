data = [1, 2, 3, 4, 5, 6, 7, 8]

print("List Before swaping element", data)
#index = 1

# print(data[1], data[-2])
#
# data[1], data[-2] = data[-2], data[1]
#
# print(data[1], data[-2])


    ## Aproach-2 ##    2 ,7 = 7, 2


temp = data[1]

data[1] = data[-2]

data[-2] = temp

print("List After Swaping element", data)