f= open("Biology.txt", "r")
f2= open("newfile3.txt", "w")
count=0
#print(f.read())
for i in f:
    a= i.replace(" ", "_").strip()
    count+=1
   # print(a,"=", count)
    d= a + "=" +str(count)
    f2.write(d +"\n")
