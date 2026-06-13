#Find largest of 3 numbers
A = int(input("Enter first number: "))
B = int(input("Enter second number: ")) 
C = int(input("Enter third number: "))
if A > B and A > C:
    print("The largest number is:", A)
elif B > A and B > C:
    print("The largest number is:", B)
else:
    print("The largest number is:", C  )