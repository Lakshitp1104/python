#Invert a dictionary (keys ↔ values)

d = {"a": 1, "b": 2, "c": 3}

invert ={}

for key in d:
    value =d[key]
    invert[value] =key 
print(invert)