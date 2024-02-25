with open("q3.1.txt", "w") as a:
    a.write("My first line\n")
    a.write("My second line")
    
    a.seek(0)
    print(a.read())

    