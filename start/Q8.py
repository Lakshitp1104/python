#Reverse a number
num = int(input("Enter number: "))
rev = 0
n = abs(num)  # handle negative numbers
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
# if original number was negative
if num < 0:
    rev = -rev
print("Reversed number:", rev)