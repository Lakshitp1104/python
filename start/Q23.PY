#Store student marks in dictionary and find topper
student ={
    "lakshit" :98,
    "amit":67,
    "bhushan":56
}
topper = ""
max =-1
for name in student:
    if student[name]> max:
        max=student[name]
        topper=name

print(topper)
print(max)