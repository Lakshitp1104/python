#Sort list without using sort()
list = [5, 2, 9, 1, 5, 6]
for i in range(len(list)):
    for j in range(len(list)-1-i):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j  ]
print("Sorted list:", list)