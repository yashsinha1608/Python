#f=open("file name","mode")  mode:- either read or write \
import os #used for deleting 
"""f=open("demo.txt","r")
data=f.read(6)
data=f.readline() #reads one line at a time

print(data)
f.close()"""

"""f=open("demo.txt","w") #writting a file  #overwrites the entire file 

f.write("This is a new inserted line") 
f=open("demo.txt","r")
print(f.read())"""

"""f=open("demo.txt","a") #adds a new line in the file 
f.write("  ADDED LINE")
f=open("demo.txt","r")
print(f.read())"""


#another way 
"""with open("demo.txt","r") as f:
    data=f.read()
    print(data)"""

os.remove("demo.txt") #used to delete a file 

