#Tạo file sale.txt

a = open('sales.txt', "w")
a.close()
#tạo file với ngày
import datetime
b = str(datetime.datetime.now())
c ="" + b + ".txt"
c = c.replace(":",'-')
c = c.replace(".","-")
d = open(c, "w")
print("đã tạo file" , c)
d.close()

# tạo file với permission
import os
import glob

e =  open("example.txt", "w")
e.close()

filepath = glob.glob("./example.txt") #lấy file direct để xài cho os
if filepath:
    f = filepath[0]


os.umask(0)
with open(os.open(f, os.O_CREAT | os.O_WRONLY, 0o777), 'w') as file:
    print("đã tạo file example.txt vs permission")



