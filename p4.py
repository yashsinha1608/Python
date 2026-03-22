#Dictionary
#used to store key:value pair
#unordered mutable and don't allow duplicate keys

info = {
    "name":"yash",
    "age":21,
    "marks":[98,95,99,93.54],
}
#print(info)
print(info["age"]) # used to fetch the value of a perticular key 
info["age"]= 87 #store a new value (changing values)


null_dict={} #created a null dictionary having no data
print(null_dict)

null_dict["name1"]="YASH" #created data after making a dictoinary  
print(null_dict)


#nested dictinary 
details={
    "name": "YASH SINHA",
    "sub":{
        "ml":93,
        "AI":91,
        "uhv":96
    }
}
print(details)
print(details["sub"])
print(details["sub"]["AI"])