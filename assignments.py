# This is assignment 1
# Program to take input from user until 0 is entered and print average. Negative input to be ignored
total = 0
cnt = 0
while True:
    num = int(input("Please enter a number (Entering Zero will terminate) : "))
    if num == 0:
        break
    elif num < 0:
        continue
    else:
        total += num
        cnt += 1
if cnt == 0:
    print(f"No numbers entered.")
else:
    print(f"Average of the entered numbers is {total/cnt}")