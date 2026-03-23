#f=open("file name","mode")  mode:- either read or write 
f=open("demo.txt","r")
data=f.read(6)
data=f.readline() #reads one line at a time

print(data)
f.close()