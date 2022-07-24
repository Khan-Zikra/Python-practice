f = open("Chemistry.txt","r")
f2= open("newfile.txt", "w")
count=0
for x in f:
    c= x.replace(" ", "_").strip()
    count+=1
    #print(c,"=",count)
    d= c + "=" + str(count)
    f2.write(d+"\n")

