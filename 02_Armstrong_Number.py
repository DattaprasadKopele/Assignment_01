#### Armstrong Number    #####

num=int(input("Enter a number= "))

def check_armstrong(num):

    order = len(str(num))
    sum= 0

    original = num
    while num> 0:
        digit = num% 10
        sum+= digit ** order
        num= num//10

    if sum == original:
        return True
        print("Number is armstrong ")

    else:
        return False
        print("Number is not armstrong ")

if check_armstrong(num):
    print("Number is armstrong")

else:
    print("Number is not armstrong")