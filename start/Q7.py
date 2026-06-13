#Count digits in a number
num = int(input("enter number:"))
count = 0
while num>0:
    num = num // 10
    count += 1
print("number of digits:", count)