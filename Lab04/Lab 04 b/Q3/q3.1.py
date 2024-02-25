def uppercasecount(filename):
    with open(filename, "r") as a:
        count = 0
        split = a.read()
        for i in split:
            if i.isupper():
                count +=1
    return count
a = "story.txt"
print(uppercasecount(a))