#1. Print each character of a string
#This program prints each character one by one.
text = "lakshit"
for char in text:
    print(char)


#2. Count total characters in a string
#This program counts total characters in a string.
name = "lakshit"
count = 0
for char in name:
    count += 1
print("The string is:" , count)

#3. Count vowels in a string 
# This program counts vowels in a string.
name = "lakshit"
count=0
for vowel in name:
    if vowel in "aeiouAEIOU":
        count += 1  
print("The number of vowels in the string is:" , count)

#4. Count consonants in a string
#  This program counts consonants in a string.
name = "lakshit"
count = 0
for consonant in name:
    if consonant not in "aeiouAEIOU":
        count += 1
print("The number of consonants in the string is:" , count)


#5. Count digits in a string 
# This program counts digits in a string.
name = "lakshit123"
count = 0
for digit in name:
    if digit.isdigit():
        count += 1
print("The number of digits in the string is:" , count)

#6. Count spaces in a string 
# This program counts spaces in a string.
name = "lakshit patil"
count = 0
for space in name :
    if space.isspace():
        count += 1
print("The number of spaces in the string is:" , count)


#7. Convert lowercase to uppercase 
# This program converts lowercase letters to uppercase.
name = "lakshit"
print(name.upper())

#8. Convert uppercase to lowercase 
# This program converts uppercase letters to lowercase.
name = "LAKSHIT"
print(name.lower())

#9. Reverse a string using loop
#  This program reverses a string.
name = "lakshit"
rev = ""
for char in name:
    rev = char + rev
print(rev)

#10. Check whether string is palindrome 
# This program checks palindrome string.
name = "lakshit"
rev = ""
for char in name:
    rev = char + rev
if name == rev:
    print("The string is palindrome")
else:
    print("The string is not palindrome")


#11. Print characters at even index
# This program prints characters at even index positions.
name = "lakshit"
for i in range(0 ,  len(name), 2):
 print(name[i])

#12. Print characters at odd index 
# This program prints characters at odd index positions.
name = "lakshit"
for i in range(1 , len(name), 2):
 print(name[i])


#13. Find frequency of character 
# This program finds frequency of a character.
name = "lakshit"
char = "a"
count = 0
for c in name:
    if c == char:
        count += 1
print(f"The frequency of '{char}' in the string is: {count}")   



#14. Remove spaces from string
#  This program removes spaces from a string.
name = "lakshit patil"
result = "" 
for char in name:
    if char != " ":
        result += char
print(result)

#15. Replace vowels with *
#  This program replaces vowels with * symbol.
name = "lakshit"
result = ""
for char in name:
    if char in "aeiouAEIOU":
        result += "*"
    else:
        result += char
        print(result)


#16. Print ASCII value of each character 
# This program prints ASCII value of characters.
name = "lakshit"
for char in name:
    print(f"The ASCII value of '{char}' is: {ord(char)}")



#17. Find longest word in sentence
#  This program finds longest word in sentence.
name = "lakshit patil is a good boy"    
words = name.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(f"The longest word in the sentence is: {longest_word}")

#18. Find shortest word in sentence 
# This program finds shortest word in sentence.
name = "lakshit patil is a good boy"
words = name.split()
shortest_word = words[0]
for word in words:
    if len(word) < len(shortest_word):
        shortest_word = word
print(f"The shortest word in the sentence is: {shortest_word}") 


#19. Count words in sentence
# This program counts words in sentence.
name = "lakshit patil is a good boy"
count =0
for word in name.split():
    count += 1
print(f"The number of words in the sentence is: {count}")



#20. Separate alphabets digits and special characters 
# This program separates alphabets, digits and special characters.
name = "lakshit123@#"
alphabets = ""
digits = ""
special_chars = ""
for char in name:   
    if char.isalpha():
        alphabets += char
    elif char.isdigit():
        digits += char
    else:
        special_chars += char
print(f"Alphabets: {alphabets}, Digits: {digits}, Special Characters: {special_chars}")


#21. Check vowel or consonant 
# This program checks vowel or consonant.

name = "lakshit"
for char in name:
    if char in "aeiouAEIOU":
        print(f"{char} is a vowel")
    else:
        print(f"{char} is a consonant")


#22. Print duplicate characters
#  This program prints duplicate characters.
name = "lakshit patil"
duplicates = ""
for char in name:
    if name.count(char) > 1 and char not in duplicates:
        duplicates += char
print(f"Duplicate characters in the string are: {duplicates}")


#23. Print unique characters
#  This program prints unique characters.
name = "lakshit patil"
unique_chars = ""
for char in name:
    if name.count(char) == 1:
        unique_chars += char
print(f"Unique characters in the string are: {unique_chars}")


# 24. Compare two strings 
# This program compares two strings.
name = "lakshit"
last_name = "patil"

if name == last_name:
    print("Strings are equal")
else:
    print("Strings are not equal")


#25. Find first non repeating character 
# This program finds first non-repeating character

name = "lakshit"
for char in name:
    if name.count(char) == 1:
        print(char)
        break


#26. Find first repeating character 
# This program finds first repeating character.
name="lakshit patil"
for char in name:
    if name.count(char) > 1:
     print("First repeating =", char)
     break


#27. Remove duplicate characters
#  This program removes duplicate characters.   
name = "lakshit patil"
result =""
for char in name:
    if char not in result:
        result+= char
print(result)

#28. Sort characters alphabetically
#  This program sorts characters alphabetically.
text = input("enter")
chars = sorted(text)
for ch in chars:
 print(ch, end = " ")

#29. Print string in reverse without slicing
#  This program prints reverse string without slicing.
text = input ("enter")
for i in range(len(text)-1, -1 ,-1):
    print (text [i] , end="")

#30. Create new string using alternate characters
#  This program creates string using alternate characters.

text = input("Enter a string: ")
result = ""

for i in range(0, len(text), 2):
    result += text[i]

print(result)