# Create a palindrome generator between 2 input values
def palindromes(start, end):
    for num in range(start, end + 1):
        s = str(num)
        if s == s[::-1]:
            yield num

# Testing
for n in palindromes(100,200):
    print (n)

