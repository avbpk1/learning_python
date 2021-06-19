# 3) Assume a list of marks in the form of strings ["30,35,45","55,60,60","-,-"] etc. Total the marks and return them
marks_list = ["30,35,45","55,60,60","90,75","1,2,3,4"]
# Without Map Function

# Without Map Function
print("Sum of Marks")
for i in marks_list:
    sum_marks = 0
    for j in i.split(','):
        sum_marks += int(j)
    print(sum_marks)
# With Map Function

print("Sum of Marks with Map Function")
for i in marks_list:
    marks = map(int,i.split(','))
    print(sum(marks))
