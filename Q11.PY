#Find largest element in a list
num= [10, 20, 5, 15, 30]
largest = num[0]
for i in num:
    if i > largest:
        largest = i
print("The largest number is:", largest)