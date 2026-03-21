#list and tuples    
marks=[82.4,23.1,213,32.1,43.1,21.12,45.6]
print(marks)
print(marks[1])

list=["mumbai",20,89.24]
print(list)
print(list[0])

#slicing is possible 
print(marks[1:4])

#list functions 
marks.append(31) #add 31 at the end 
marks.sort() #sort in assending order
marks.sort(reverse=True) #sort in decending order
marks.reverse() #reverse the list
marks.insert(2,5678) #insert 5678 at index 2
marks.remove(20) #remove the first occurance of 20 frm the list 
marks.pop(3) #remove element from idx 3


