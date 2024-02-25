with open("q3.5.txt","w") as a:
    a.write("My first line\n")
    a.write("My second line\n")
with open("q3.4.txt","r+") as a:
    a.seek(0,2)
    print('file handle at:', a.tell())
    a.write("\nDemonstrating tell")
    a.seek(0)
    print('file handle at:', a.tell())
    print('***Printing File Content***')
    print(a.read())
    print('***Done***')
    print('file handle at:', a.tell())