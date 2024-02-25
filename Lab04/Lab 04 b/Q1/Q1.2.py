with open("story.txt", "r") as a:
    count = 0
    for line in a:
        if not line.startswith("T"):
            count+=1
    print("No of lines not starting with T:", count)

            