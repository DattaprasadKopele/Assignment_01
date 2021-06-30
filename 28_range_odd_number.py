'''Odd Number in range'''


n=int(input("Enter a number: "))

for x in range(1, n):
    if x%2 != 0:
        print("Odd no.= ", x)
