# Accept 5 numbers from user. Add them up. If invalid number is entered , ignore and move. Prog stops after 5 inputs
i = 1
sum = 0
while i <= 5:
    try:
        entered_num = int(input("Please enter number " + str(i) + ":"))
        sum += entered_num
        i += 1
    except:
        print(f"Entered number is Invalid! Continuing to next")
        i += 1
print(f"Sum of the entered numbers is : {sum}")