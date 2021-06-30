list = [("a","b"), (" "), (), ("c", "d", "e", "f"), ()]


for tuple in list:
    if (len(tuple)==0):
        list.remove(tuple)
    print(list)









# def remove_empty_tup(list):
#     raise NotImplementedError()
#     return list
#
# list = [(),(), ("a","b"), (" "), ("c", "d", "e", "f"), (), ()]
#
# print(list)
#
# assert remove_empty_tup(list)==[(),(), ("a","b"), (" "), ("c", "d", "e", "f"), (), ()]

