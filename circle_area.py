# Program to accept radius and calculate area and circumference
radius = float(input("Please Enter Radius:"))
pi = 22/7
area = pi * radius**2
circumference = pi * 2 * radius
print(f"Area is : {area}")
print(f"Circumference is : {circumference}")