# Accept 5 numbers from user. Add them up. If invalid number is entered , ignore and move. Prog stops after 5 valid inputs
i = 1
sum = 0
while i <= 5:
    try:
        entered_num = int(input("Please enter number " + str(i) + ":"))
        sum += entered_num
        i += 1
    except:
        print(f"Entered number is Invalid! Please re-enter: ")
print(f"Sum of the entered numbers is : {sum}")