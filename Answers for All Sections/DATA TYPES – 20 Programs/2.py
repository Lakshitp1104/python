#1. Integer Type Example
num =5
print(type(num))

#2. Float Type Example
num = 3.14
print(type(num))



#3. String Type Example
Name = "Lakshit"
print(type(Name))

#4. Boolean Type Example
is_student = True
print(type(is_student))

#5. List Type Example
numbers = [1, 2, 3, 4, 5]
print(type(numbers))

#6. Tuple Type Example
num = (1, 2, 3, 4, 5)
print(type(num))

#7. Dictionary Type Example
student ={
    "name": "Lakshit",
    "age": 21,
    "address": "pune",
}
print(type(student))

#8. Set Type Example
num={1,2,3,4,5}
print(type(num))


#9. Print Type of Variable
name = "Lakshit"
print(type(name))

#10. Take Integer Input
num =int(input("Enter an integer: "))
print("You entered:", num)


#11. Take Float Input
num =float(input("Enter a float: "))
print("You entered:", num)


#12. Convert String to Int
str_num ="123"
int_num =int(str_num)
print(int_num)

#13. Convert int to Float
int_num = 10
float_num = float(int_num)
print(float_num)


#14. Convert List to Tuple
num =[1, 2, 3, 4, 5]
tuple_num = tuple(num)
print(tuple_num)

#15. Convert Tuple to List
tuple_num = (1, 2, 3, 4, 5)
list_num = list(tuple_num)
print(list_num)

#16. Multiple Data Types in One Program
name= "Lakshit"
age = 21
is_student = True
print(type(name), type(age), type(is_student))

#17. Check Boolean Values
x = 10 > 15
print(x)

#18. String Concatenation
name = "Lakshit"
last_name = "Patil"
print(name + " " + last_name) # This will concatenate the strings without raising an error

#19. List Indexing
numbers = [1, 2, 3, 4, 5]
print(numbers[0])

#20. Dictionary Access
student ={
    "name": "Lakshit",
    "age": 21,
    "address": "pune",
}
print(student["age"])