#1. Print numbers from 1 to 10 using while loop 
# This program prints numbers from 1 to 10 using a while loop.
i=1
while i <= 10:
    print (i)
    i+=1

#2. Print numbers from 10 to 1
#  This program prints numbers in reverse order from 10 to 1.

i = 10
while i >= 1:
    print(i)
    i-=1

#  3. Print even numbers from 1 to 100 
# This program prints all even numbers between 1 and 100.
i=2
while i <=100:
    print(i)
    i+=2

#4. Print odd numbers from 1 to 100
#  This program prints all odd numbers between 1 and 100.
i=1
while i <=100:
    print(i)
    i+=2

#5. Find sum of first n numbers
#  This program calculates the sum of first n natural numbers.
n = int(input(" :"))
i= 1
total =0
while i <=n:
    total+=i
    i+=1
print("sum=", total)

#6. Find factorial using while loop 
# This program finds factorial of a number.
num = int(input(";"))
fact =1
i=1
while i <=num:
    fact*= i
    i+=1
print(fact)

#7. Print multiplication table using while loop 
# This program prints multiplication table of a number.
num = int(input("/"))
i=1
while i<=10:
    print(num,"X ",i ,"=", num*i)
    i +=1


#8. Reverse a number using while loop 
# This program reverses a given number
num =int(input())

rev =0

while num>0:
    digit = num%10
    rev =rev * 10 + digit
    num =num //10
    print(rev)

#9. Check palindrome number using while loop 
# This program checks whether a number is palindrome or not.
num = int(input())
temp =num
rev = 0
while num >0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if temp == rev:
     print("Palindrome Number") 
else:  
     print("Not Palindrome Number")


#10. Count digits in a number
#  This program counts total digits in a number.

num = int (input(""))
count = 0

while num > 0:
    num = num // 10 
    count+=1
print(count)

#11. Find sum of digits 
# This program finds the sum of digits of a number.
num = int(input("Enter number: ")) 
total = 0 
while num > 0:

  digit = num % 10    
  total += digit    
  num = num // 10 
print("Sum of digits =", total)

#12. Print Fibonacci series using while loop
#  This program prints Fibonacci series.
n =10

a = 0
b =1
i =1

while i<=n:
    print(a)
    c=a+b
    a=b
    b=c
    i+=1

#13. Check Armstrong number 
# This program checks whether a number is Armstrong number.
num = int(input("Enter number: "))
temp = num 
total = 0 
while temp > 0:    
    digit = temp % 10    
    total += digit ** 3    
    temp = temp // 10 
    if total == num:    
        print("Armstrong Number") 
else:   
        print("Not Armstrong Number")

#14. Keep taking input until user enters 0
#  This program continuously takes input until user enters 0.
num =1

while num!= 0:
    num = int(input(""))

#15. Create simple login system
#  This program checks username and password.

username = "lakshit"
password ="1234"

u = input("Enter username: ") 
p = input("Enter password: ")

while u != username or p!= password:
     print("Invalid Login")    
     u = input("Enter username: ")    
     p = input("Enter password: ")
     print("Login Successful")


#16. Guess the number game 
# This program creates a simple number guessing game.
secret = 7 
guess = 0 
while guess != secret:    
    guess = int(input("Guess number: ")) 
    print("Correct Guess")

#17. Print pattern using while loop 
# This program prints star triangle pattern.
i =1
while i<=5:
    print("*"* i)
    i +=1

#18. Find GCD of two numbers 
# This program finds greatest common divisor of two numbers.

a = int(input("Enter first number: ")) 
b = int(input("Enter second number: "))

while b!= 0:
    a.b = b.a% b
print("GCD= ",a)

#19. Calculate power of a number 
# This program calculates power of a number.
base = int(input("Enter base: ")) 
exp = int(input("Enter exponent: ")) 
result = 1 
i = 1 
while i <= exp:    
    result *= base    
    i += 1 
print("Answer =", result)

#20. Menu-driven calculator using while loop 
# This program creates a simple calculator menu.
choice = 1 
while choice != 0:    
    print("1.Add")    
    print("2.Subtract")    
    print("0.Exit")    
    choice = int(input("Enter choice: "))    
    if choice == 1:        
        a = int(input("Enter first number: "))        
        b = int(input("Enter second number: "))        
        print("Sum =", a + b)    
    elif choice == 2:        
     a = int(input("Enter first number: "))        
     b = int(input("Enter second number: "))        
     print("Difference =", a - b)    
    elif choice == 0:        
      print("Program Ended")    
    else:        
       print("Invalid Choice")