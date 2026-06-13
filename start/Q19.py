#Merge two lists
list1=[1,2,3]
list2=[4,5,6]
new_list=list1+list2
print(new_list)

#------------------OR------------------

list1=[1,2,3]
list2=[4,5,6]

new_list=[]

for i in list1:
 new_list.append(i)
for i in list2: 
 new_list.append(i)
print(new_list)