#Accept a string which contains a list of numbers separted by comma and display the average of the numbers.
num_string = input("Enter a list of numbers separated by commas :")
#num_list = [n for n in num_string] - Syntax
num_construct = ''
num_list = []
total = cnt = 0
for n in num_string:
    if n == ',' and num_list != []:
        #print(num_construct)
        num_list.append(int(num_construct))
        num_construct = ''
        continue
    else:
        num_construct += n
if num_list != []:
    num_list.append(int(num_construct))
    for n in num_list:
        total += n
        cnt += 1
        print(total/cnt)
else:
    print("Invalid Input Entered")

