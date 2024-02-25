def display_words(filename):
    with open(filename, "r") as a:
        for line in a:
            word = line.split()
            for i in word:
                if len(i) <4:
                    print(i)
    return ""
a = "story.txt"
print(display_words(a))