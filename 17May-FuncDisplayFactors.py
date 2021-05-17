# 1) Create a function that takes a number and displays its factors
def display_factors(number):
    factors = [x for x in range(1,(number//2)+1) if number%x == 0]
    print(factors)
display_factors(20)
# for x in range(1,number//2 + 1):
#     print(x)
#     if number%x == 0:
#         factors.append(x)

