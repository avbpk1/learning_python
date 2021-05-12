# This is assignment 4
# Program to accept Shape and take necessary inputs and calculate area

while True:
    n = int(input("Please enter shape ( 1 for Circle 2 for Rectangle and 3 for Square: "))
    if n == 1:
        radius = float(input("Please enter radius: "))
        area = 22*radius*radius/7
        break
    elif n == 2:
        length = float(input("Please enter length of rectangle:"))
        width = float(input("Please enter width of rectangle:"))
        area = length * width
        break
    elif n == 3:
        side = float(input("Please enter side of the square:"))
        area = side * side
        break
    else:
        print("Invalid input ")
        continue

print(f"Area for the provided input is {area}")
