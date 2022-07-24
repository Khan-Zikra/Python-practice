f=open("physics.txt","r")
f2=open("newfile2.txt", "w")
count=0
#print(f.read()) 
for x in f:
    c= x.replace (" ", "_").strip()
    count+=1
     # print(c,"=" ,count)
    d=c + "=" +str(count)
    f2.write(d+"\n")
    
   
