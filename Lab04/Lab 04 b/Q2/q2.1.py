def wordscount(filename):
    with open(filename, "r") as a:
        count = 0
        for line in a:
            word = line.split()
            for i in word:
                count+=1
    print("Total words are: ", end="")
    return count
a = "story.txt"
print(wordscount(a))
