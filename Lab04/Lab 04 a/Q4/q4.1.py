import os
oldname="details.txt"
newname="new_details.txt"
if os.path.isfile(newname):
    print("File tồn tại r")
else:
    os.rename(oldname,newname)