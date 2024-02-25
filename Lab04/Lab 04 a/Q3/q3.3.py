with open("q3.3.txt", "w") as a:
    a.write("My first line\n")
    a.write("My second line\n")
with open("q3.3.txt","rb") as a:
    a.seek(3)
    print(a.read(5).decode("utf-8"))
    a.seek(10, 1)
    print(a.read(6).decode("utf-8"))

    