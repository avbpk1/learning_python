# ass2 - Sort a set of names by length after stripiing spaces.
def strip_spaces_len(str):
    return len(str.replace(' ',''))


names = ['Venkat eswar','Rama Kris h            na','Krish','Venu Ayy','Srikanth Prag ada']

for name in sorted(names,key = strip_spaces_len):
    print(name)
