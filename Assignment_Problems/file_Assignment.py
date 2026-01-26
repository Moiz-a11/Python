

# with open("names.txt","w") as file:
#     print("enter 5 names :")
#     for i in range(5):
#         name =input()
#         file.write(name)


    
# with open("names.txt","r") as file:
#     for line in file:
#         print(line," ")  




with open("log.txt","a") as file:
    print("new entry added successfully")


with open("log.txt","r") as file:
    for content in file:
        print(content," ")