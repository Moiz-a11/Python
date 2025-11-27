
# class Student:
#     name="moiz"
#     college="GHRCEM"
#     year="SY"

#     def display():
#         print("displaying values")
# std1 = Student() # Student() shows init method is called 
# std2 = Student()
# print(std1.name)
# print(std1.year)

#2]
# class Student:
#     def __init__(self): # self parameter is by default called as default constructor
#         print("constructor was called")

# std = Student()

#3]

class Car:

    model="average"

    def __init__(self,name,cgpa): # parameterized constructor
        self.name =name
        self.cgpa=cgpa

    def get_cgpa(self):
            return self.cgpa



car1 = Car("toyota",10)
print(car1.name)

print(car1.get_cgpa())
print(Car.model) # we can access class attributes direct  by  class name , but using class name we can access only class attributes
