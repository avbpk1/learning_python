# 1) Assume a list of strings which may contain numbers and non numbers and display sum of the numbers.
# -- clue -- use filter and pick up numbers and sum them.

# v1 code without filter function
str_list = ['123','ss1','456','ww','00']
print(f"Input list of values : {str_list}")
sum = 0
for s in str_list:
    if s.isdigit():
        sum += int(s)
print(f"Sum without using Filter : {sum}")

# v2 code with filter function
sum = 0
for s in filter(str.isdigit, str_list):
    sum += int(s)
print(f"Sum using Filter : {sum}")
