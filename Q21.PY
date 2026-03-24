#Count frequency of each element in list

nums =[1,2,3,4,5,1,2,3]

frequency={}

for num in nums:
 if num in frequency:
  frequency[num] +=1
 else:
  frequency[num] =1

print(frequency)
  
