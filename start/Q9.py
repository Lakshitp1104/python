#Check palindrome number
num = (input("Enter number: "))
if num ==num[::-1]:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")