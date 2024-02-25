with open("q3.4.txt","w") as a:
    a.write("My first line\n")
    a.write("My second line\n")
with open("q3.4.txt","rb") as a:
    print(a.read(8).decode('utf-8'))
    a.seek(-5,1)
    print((a.read(10).decode('utf-8')))