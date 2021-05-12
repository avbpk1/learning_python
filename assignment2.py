# This is assignment 2
# Program to accept 2 numbers and display common factors
num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))
common_factors = ""
if num1 <= num2 and num1 > 0:
    for i in range(2,1 + num1//2):
        if num1 % i == 0 and num2 % i == 0:
            common_factors = common_factors + str(i) + ","
else:
    for i in range(2,1 + num2//2):
        if num1 % i == 0 and num2 % i == 0:
            common_factors = common_factors + str(i) + " "

print(f"Common factors for the entered numbers {num1} and {num2} : {common_factors }")