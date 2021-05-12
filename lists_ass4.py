#program to accept user input until user enters 0 and present them in sorted order

i = 1
num_list = []
while i != 0:
#   print(f"Value of i is {i}")
    i = int(input("Enter a number [0 to end]: "))
#    print(f"Value of i is {i}")
    num_list.append(i)
num_list.sort()
print(num_list)