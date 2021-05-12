# Program to accept main string and substring and display where the substring is present in main string
# All positions to be provided
main_str = input("Enter main string: ")
sub_str = input("Enter sub string: ")
i = 0
cnt = 0
while main_str[i:].find(sub_str) >= 0:
    cnt += 1
    i += main_str[i:].find(sub_str) + len(sub_str)
print(f"Number of occurances of {sub_str} in {main_str} is: {cnt}")
# Continuation to display how many upper case letters are there
j = 0
cnt_upper = 0
for l in main_str:
    if l.isupper():
        cnt_upper += 1
print(f"Number of upper case characters in main string {main_str} is: {cnt_upper}")
