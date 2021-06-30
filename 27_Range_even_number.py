'''Range Even Number'''

n=int(input("Enter a number: "))

for x in range(1, n):
    if x%2 == 0:
        print("Even number= ", x)

# for x in range(1, n):
#     if x%2 != 0:
#         print("Odd no.= ", x)
