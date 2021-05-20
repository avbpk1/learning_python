# -- ass4 -- use map to extract all alphabets from each string in a list. Use map and a function

def ext_alpha(word_str):
    new_word = ''
    for c in word_str:
        if c.isalpha():
            new_word += c
    return new_word
words =  ['Ab12c','x12y2','sdfds33&']
for word in words:
    alpha_extract = map(ext_alpha,word)
    print(alpha_extract)

# gives following output -- please explain
# <map object at 0x000001C3B608ED90>
# <map object at 0x000001C3B608ED30>
# <map object at 0x000001C3B608EDC0>
#
# Process finished with exit code 0
