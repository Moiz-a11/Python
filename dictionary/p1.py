
data ={

    "name":"moiz",
    "cgpa":8.5,
    "subjects":["math","chemistry","physics"]

}
data["cgpa"] =9.5
#print(data)
# methods of dictionary

#print(data.keys())
#.get()>> continues code safely

data.update({
    "status":"unmaried"
})
print(data)