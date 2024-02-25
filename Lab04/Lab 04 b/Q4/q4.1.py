def hash_display():
    with open("matter.txt","r") as a:
        for line in a:
            words = line.strip()
           
            for i in words:
                print(i, end="#")
    return ""
hash_display()                
            