#Function to return factorial

def factorial(n):
    if n < 0:
        return "Not defined for negative numbers"
    
    result = 1
    
    for i in range(1, n + 1):
        result *= i   # result = result * i
    
    return result

print(factorial(5))