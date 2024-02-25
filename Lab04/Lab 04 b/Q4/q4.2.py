def JTOI():
    with open("WORDS.txt","r") as a:
        for line in a:
            line = line.replace("J", "I")
            print(line, end="")
JTOI()
            