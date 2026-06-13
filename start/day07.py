# Create a new "demo.txt" using python add the following data in to 
# hi everyone
# we are learing file handling in python I/O using java 
# i like programming in java
with open("demo.txt", "w") as f:
    # Write the data to the file
    f.write("hi everyone\n")
    f.write("we are learing file handling in python I/O using java \n")
    f.write("i like programming in java\n")

# WAF the replace all occurences of java with python in the file
with open("demo.txt", "r") as f:
    data = f.read()
    new_data = data.replace("java", "python")
with open("demo.txt", "w") as f:
    f.write(new_data)
print(new_data)

# search if the word "learing" exit in the file or not
word = "learing"
with open("demo.txt", "r") as f:
    data = f.read()
    if (data.find(word) != -1):
        print("is found in the file")
    else:
        print("is not found in the file")