#Check if a number is prime
num = int(input("enter number:"))
if num<=1:
    print("not prime")
else:
    is__prime = True
    for i in range (2,num):
        if num % i == 0:
            is__prime = False
            break
    if is__prime:
        print("Prime")
    else:
        print("Not Prime")