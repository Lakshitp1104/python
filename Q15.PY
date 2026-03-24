#Remove duplicates from list
list =[1,2,3,4,5,6,7,8,9,10,1,2,3,4,0,5]
newlist=[]
for i in list:
    if i not in newlist:
        newlist.append(i)
print(newlist)