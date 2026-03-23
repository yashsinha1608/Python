#f=open("file name","mode")  mode:- either read or write 
f=open("demo.txt","r")
data=f.read()
print(data)
f.close()