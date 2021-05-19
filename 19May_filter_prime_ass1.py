# select prime numbers from a list of numbers using filter
def isprime(n):
    for i in range(2,n//2 + 1):
        if n % i == 0:
            return 0
    return 1
nums = [3,4,7,9,10,25,47]
for n in filter(isprime,nums):
    print(n)