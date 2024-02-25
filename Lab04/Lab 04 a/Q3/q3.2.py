with open("q3.2.txt", "w") as a:
    a.write("My first line\n")
    a.write("My second line\n")
    
    a.seek(0,2)
    a.write("This content is added to the end of the file")
    a.seek(0)
    print(a.read())

    