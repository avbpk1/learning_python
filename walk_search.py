#Accept starting directory and search string and display all files where the name contains search string. Display count also.
import os
import sys
# starting_directory = 'c:\classroom\may6'

if len(sys.argv[1]) > 0:
    starting_directory = sys.argv[1]
else:
    starting_directory = os.getcwd()

# search_str = 'practice'
if len(sys.argv[2]) > 0:
    search_str = sys.argv[2]
else:
    search_str = 'test'

file_cnt = 0
all_files = os.walk(starting_directory)
for dirname, directories,files in all_files:
    print(f"Directory Name:{dirname}")
    for file in files:
        if file.find(search_str,1,len(file)) != -1:
            print(file)
            file_cnt += 1
    if file_cnt == 0:
        print(f"No matches found.")
    else:
        print(f"File Count :{file_cnt}")
        file_cnt = 0 #reset variable to 0
