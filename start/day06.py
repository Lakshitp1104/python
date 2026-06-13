 # WAF to print thew length of a list (list is the parameter)

Names =["lakshit","patil","karkit", "bhushan","shirish","mehul"]

def print_len(Name):
   print(len(Name))

print_len(Names)

# #  WAF to print element of a list in a single line (list is the parameter) Names = ["lakshit", "patil", "karkit", "bhushan", "shirish", "mehul"]

def print_list(Names):  
   for item in Names:    
      print(item, end=" ")
      
print_list(Names)


# # WAF to find the factorial of a n (n is the parameter)
def factorial(n):    
    fact =1
    for i in range(1 ,n+1):
        fact *= i   
        print(fact) 
        
factorial(5)




# # WAF to convert usd to in
def convert_usd_to_inr(usd):     
     inr = usd * 83
     print(usd, "USD is equal to", inr, "INR") 

convert_usd_to_inr(100) 

# RECURSION

def show(n):
    if n == 0:
        return
    print(n)
    show(n-1)

show(5)

# write a recursive function to calculate the sum of first n natural numbers
def sum(n):
    if n == 0:
         return 0
    return sum(n-1) + nx
print(sum(5))