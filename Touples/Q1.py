#Q] list all unique courses
info=[
    ("sk","math"),
    ("patel","iqc"),
    ("ansari","english"),
    ("pathan","oop"),
    ("rehan","english")
]
# newSet=set()
# for i in info:
#   newSet.add(i[1])


# print(newSet) 
    
  #Q.2] list who inrolled in english

# for i in info:
#     if(i[1]=="english"):
#         print(i)
 # Q.3] create dictionary  (student , set of courses)

dict ={}

for name,subject in info:
    if(dict.get(name)==None):
        dict.update({name : set()})
        dict[name].add(subject)
    else:   
        dict[name].add(subject)

print(dict)