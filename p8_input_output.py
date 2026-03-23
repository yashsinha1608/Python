#f=open("file name","mode")  mode:- either read or write 
"""f=open("demo.txt","r")
data=f.read(6)
data=f.readline() #reads one line at a time

print(data)
f.close()"""

f=open("demo.txt","w") #writting a file
f.write("This is a new inserted line")  #overwrites the entire file 

f=open("demo.txt","r")
print(f.read())


