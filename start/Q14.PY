#Count even and odd numbers in list
num= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = 0
odd_count = 0
for i in num:
    if i % 2 == 0:
        print("even number:", i)
        even_count += 1
    else:
        print("odd number:", i)
        odd_count += 1
print("Total even numbers:", even_count)
print("Total odd numbers:", odd_count)