# This is assignment 3
# Program to accept 3 numbers and print largest among them
num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))
num3 = int(input("Please enter third number: "))
largest_num = num1
if num2 >= num3 and num2 >= num1:
    largest_num = num2
elif num3 >= num2 and num3 >= num1:
    largest_num = num3
print(f"Largest number is  {largest_num}")