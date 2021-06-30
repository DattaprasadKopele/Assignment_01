'''Q.4 Python program for fibonacci numbers'''


n=int(input("Enter a no= "))
n1, n2 = 0, 1
count = 0

# l1=[]

if n <= 0:
    print("Invalid, please enter a positive integger")
elif n == 1:
    print("Fabonacci sequence upto", n,":")
    print(n1)
else:
    print("Fabonacci sseries upto", n,":")

    while count < n:
        print(n1)
        total= n1 + n2
        n1 = n2
        n2 = total
        # l1.append(total)
        count += 1



# print(l1)
# print(sum(l1))


'''

n= int(input("Enter a number="))
x=0
y=1
z=0

while(z<=n):
    print(z)
    x=y
    y=z
    z=x+y

'''


'''

def generatefab():
    n2=1
    n3=1
    while True:
        n1 = n2
        n2 = n3
        n3 = n1 + n2
        yield n1

a = generatefab()
for i in range(11):
    # print(next(a),)

    print(next(a), end=" ")


'''
