# select strings that contain a special character using filter -- ask about this
def has_special(str1):
    if not str1.isalnum():
        return True
words = ['nospecialchar','£ is special','2343 2 has space special','a11!','ffghfh','343425234']

for word in filter(has_special,words):
    print(word)
