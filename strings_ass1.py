# Program to accept a string from user and check whether it is a valid product code or not
# Valid product codie is made of 2 alphabets followed by 4 digits
product_code = input("Please enter a product code: ")

if product_code[0:2].isalpha() and product_code[2:].isdigit() and len(product_code) == 6:
    print("Valid Product Code")
else:
    print("Invalid Product Code")