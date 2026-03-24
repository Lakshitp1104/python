# Function to check palindrome string

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))