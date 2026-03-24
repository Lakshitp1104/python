#Find second largest number
nums = [1,2,3,4,5,6,7,8,9,10]
first = second = float('-inf')

for num in nums:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print("Second largest:", second)