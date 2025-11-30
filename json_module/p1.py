#json means java script object notation 
import json
#json.loads() to load the data
#json.dumps() to store the data  

# json_str = '{"name": "skaikh", "isTeacher": true}'


# py_obj = json.loads(json_str) #convert to python string
# print(type(py_obj),py_obj)

#2]
# with open(r"c:\mahadbtDocuments\Python\json_module\data.json", "r") as f:
#     py_obj=json.load(f)
#     print(py_obj)

#3]
data={
    "name":"ayesha",
    "Age":18,
    "isTeacher":True
}
with open(r"c:\mahadbtDocuments\Python\json_module\data.json", "w") as f:
    json.dump(data,f, sort_keys=True)