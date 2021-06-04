# 1) Accept a file name from user and display the files after removing white space and converting file to upper case.
# Removing leading and trailing spaces and convert it to uppercase
# 2) Accept a file and display the words in the file in sorted order
filename = input("Please enter a file name:")
f = open(filename, 'rt')
lines = map(str.strip, f.readlines())
for line in lines:
    print((line.upper()))

f.close()

f = open(filename, 'rt')
lines = map(str.strip, f.readlines())

for line in lines:
    res = sorted(line.split())
    print(str(res))

f.close()
