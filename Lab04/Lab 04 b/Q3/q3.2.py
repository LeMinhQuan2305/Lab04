def thisthesecount(): 
    with open("article.txt","r") as a:
        count =0
        for line in a:
            word = line.split()
            for i in word:
                if i == "this" or i == "these":
                    count+=1
    return count
print(thisthesecount())
