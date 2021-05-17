# Create a function called print_table which takes the number and length and prints a table for the number

def print_table(number,length):
    for i in range(1,length+1):
        print(f"{number} X {i} = {i*number}")

print_table(26,20)