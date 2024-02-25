#Q2-1
with open("q2.2.txt", "w") as a:
    a.write("This is new content")
    print("Done writing")
with open("q2.2.txt", "r") as a:
    for line in a:
        print(line)
#Q2-2
with open("q2.2.txt", "a") as a:
    
    print("Opening again..")
    b = "This is overwritten content"
    a.write(b)
    print(b)
#Q2-3
arr = ["Name: Emma\n", "Adress: 221 Baker Street\n", "City: London\n"]
with open("q2.3.txt", "w") as a:
    a.writelines(arr)
with open("q2.3.txt", "r") as a:
    for line in a:
        print(line, end="")
 

    
