#Find smallest element in a list
num=[1,0,2,3,4,5]
small = num[0]
for i in num:
    if i < small:
        small = i
print("The smallest number is:", small)