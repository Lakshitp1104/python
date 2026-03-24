#Reverse a list (without using reverse())
list =[1,2,3,4,5,6,7,8,9,10]
newlist=[]
for i in range(len(list)-1,-1,-1):
    newlist.append(list[i])
    print(newlist)