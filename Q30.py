#Function to count vowels in string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0

    for ch in s:
        if ch in vowels:
            count +=1
    return count

print(count_vowels("hello"))     
print(count_vowels("Python"))    