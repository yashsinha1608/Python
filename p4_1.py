#dictionary 
info = {
    "name":"yash",
    "age":21,
    "marks":[98,95,99,93.54],
}

print(info.keys()) #give all keys
print(info.values()) #give all values
print(info.items()) #give alll key:value pairs as tupples 
print(info.get("name")) #give the value
info.update({"city":"NAGPUR"}) # UDATE THE VAUE  
print(info)