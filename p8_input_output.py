#f=open("file name","mode")  mode:- either read or write 
f=open("demo.txt","r")
data=f.read(6)
print(data)
f.close()