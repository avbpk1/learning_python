# Accept numbers until user enters 0 and display numbers in sorted order. Clue -- use list.sort()
num_list = []
n = int(input("Enter a number [0 to End Input] :"))
while n:
    num_list.append(n)
    n = int(input("Enter a number [0 to End Input] :"))

even_list = [n2 for n2 in num_list if n2%2 == 0]
odd_list = [n2 for n2 in num_list if n2%2 != 0]
print(sorted(even_list))
print(sorted(odd_list))
# print(f" Sorted order of even numbers : {sorted(even_list)}  \n Sorted order for odd numbers : {sorted(odd_list)}")