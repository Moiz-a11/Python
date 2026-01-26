
#Q.1]
# with open("names.txt","w") as file:
#     print("enter 5 names :")
#     for i in range(5):
#         name =input()
#         file.write(name)


    
# with open("names.txt","r") as file:
#     for line in file:
#         print(line," ")  



#Q.2]
# with open("log.txt","a") as file:
#     print("new entry added successfully")


# with open("log.txt","r") as file:
#     for content in file:
#         print(content," ")



#Q3.]
#list comprehension
# list =[5,10,15,20,25]
# new_list =[num for num in list if num > 15]
# print(new_list)



#Q.4]
# import json
# cities={
#     "aurangabad":500000,
#     "mumbai":100000000,
#     "delhi":30000000
# }

# with open("cities.json","w") as file:
#     json.dump(cities,file,indent=4)

# with open("cities.json","r") as file:
#     data=json.load(file)

# print("cities with population")

# for city , population in data.items():
#     print(f"{city}:{population  }")


# new_city =input("enter new city")
# new_population =input("enter population of city ")

# # Update dictionary

# data[new_city]= new_population

# with open("cities.json","w") as file:
#     json.dump(data,file,indent=4)


# print("Updated city data saved to cities.json")



#Q.5]

try:
    with open("data1.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("file not found")
# FileNotFoundError is a built-in Python exception that occurs when:

# You try to open a file

# AND the file does not exist in the given location