# select strings that contain more than 2 upper case letters.
def count_upper(s):
    count = 0
    for ch in s:
        if ch.isupper():
            count += 1

    return count > 2

words = ['sdfasW','EERTRETwww0','23324324','WWW']

for word in filter(count_upper,words):
    print (word)