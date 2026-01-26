
# class BankAccount:
#     def __init__(self,owner_name,account_number,balance=0):
#         self.owner_name=owner_name
#         self.account_number =account_number
#         self.balance=balance

#     def deposit(self,amount):

#         self.balance = self.balance+amount
#         print(f"{amount} deposite successfully")

    
#     def withdraw(self,amount):
#         if amount > self.balance:
#             print("insufficient balance")
#         else:

#             self.balance = self.balance-amount
#             print(f"{amount} withdrawn successfully. ")

#     def check_balance(self):
#         print("current balance :",self.balance)


# account1=BankAccount("ayesha",143,2000)


# account1.deposit(50000)

# account1.check_balance()

# account1.withdraw(3000)

# account1.check_balance()

# account2=BankAccount("Moiz",143,0)

# print("account number: ",account2.account_number)
# print("name : ",account2.owner_name)
# account2.check_balance()



#Q.2]

# class Book:

#     def __init__(self,title, auther):
#         self.title=title
#         self.auther=auther
#         self.reviews=[]


#     def Add_reviews(self,review):
#         self.reviews.append(review)
#         print(f"{review} added successfully")

#     def Count_reviews(self):
#         return len(self.reviews)
    
#     def Display_reviews(self):
#         for item in self.reviews:
#             print(item)



# book1 = Book("fire","john Due")

# book1.Add_reviews("nice book")
# book1.Display_reviews()
# print("total_reviews=" , book1.Count_reviews())



# book1.Add_reviews("got inspiration")
# book1.Display_reviews()
# print("total_reviews=" , book1.Count_reviews())

#Q.3]

# class Student:

#     def __init__(self,name,roll,mark):
#         self.__name=name
#         self.__roll=roll
#         self.__mark=mark

#     def get_name(self):
#         return self.__name
    
#     def get_mark(self):
#         return self.__mark
    
#     def get_roll(self):
#         return self.__roll
    

#     def set_name(self,name):
#         if name !="":
#             self.__name=name

#         else:
#             print("name must not empty")

#     def set_roll(self,roll):
#         if 1<= roll<=100:
#             self.__roll=roll
#         else:
#             print("roll_no must betwee 1 and 100")


#     def set_mark(self,mark):
#         if mark>0:
#             self.__mark=mark

#         else:
#             print("marks must  be positive")   

#s1 = Student("moiz",29,99)
# print(s1.get_name())
# print(s1.get_roll())
# print(s1.get_mark())

#print(s1.set_mark(-9))

#Q.4]

# class Shape:
#     def area(self):
#         print("area method is not for shape class")
 

# class Circle (Shape):
#     def __init__(self,r,pi):
#         self.pi=pi
#         self.r=r

#     def area(self):
#         return self.pi*self.r*self.r

# class Rectangle (Shape):
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b

#     def area(self):
#         return self.l*self.b

# class Triangle  (Shape):
#     def __init__(self,b,h):
#         self.b=b
#         self.h=h
#     def area(self):
#         return 0.5*self.b*self.h
    


# t1=Triangle(5,5)
# print("Triangle area = ",t1.area())



# c1=Circle(5,3.14)
# print("circle area = ",c1.area())


#Q.5]
# class Vehicle:
#     def __init__(self,brand,model):
        
#         self.brand=brand
#         self.model=model

# class Car(Vehicle):
#     def __init__(self,brand,model,seats):
#         super().__init__(brand, model)  # call base class constructor
#         self.seats=seats

#     def Display_info(self):
#         print("brand = ",self.brand)
#         print("modeol = ",self.model)

# class Bike(Vehicle):

#     def __init__(self,brand,model,engine):
#         super().__init__(brand, model)  # call base class constructor
#         self.engine=engine


#     def Display_info(self):
#         print("brand = ",self.brand)
#         print("modeol = ",self.model)

# b1=Bike("yamaha","2022","high")
# b1.Display_info()

#from abc import ABC, abstractmethod 

# abc = Abstract Base Classes module in Python

# ABC → used to create an abstract class

# abstractmethod → decorator used to declare abstract methods


#Q.6]

#class Employee(ABC):
    
    #@abstractmethod
    #def Calculate_salary(self):
       # pass

#     pass means do nothing
# Used as a placeholder because:
# Abstract methods do not contain logic
# Actual implementation is given in subclasses

# class Intern(Employee):
#     def __init__(self,stipend):
#         self.stipend=stipend
#     def Calculate_salary(self):
#         return self.stipend
 
# class Full_time_employee(Employee):
#     def __init__(self,monthly_salary):
#         self.monthly_salary=monthly_salary

#     def Calculate_salary(self):
#         return self.monthly_salary
       
# class Contract_employee(Employee):

#     def __init__(self,day_rate,days_worked):
#         self.day_rate=day_rate
#         self.days_worked=days_worked

#     def Calculate_salary(self):
#         return self.day_rate*self.days_worked

# e1=Intern(100000)
# print(e1.Calculate_salary())
# e2=Contract_employee(5,2000)
# print(e2.Calculate_salary())


#Q.7]

# class Person:
#     def __init__(self,name,age=None,address=None): # Default parameters allow arguments to be optional.
#         self.name =name,
#         self.age =age,
#         self.address =address


#     def display(self):
#         print("name=",self.name)
#         print("age=",self.age)
#         print("address=",self.address)

# p1 = Person("moiz",20)
# p1.display()

#Q.8]
# class Player:
#     Player_count=0

#     def __init__(self,name,level):
#         self.name=name
#         self.level=level
#         Player.Player_count+=1



# p1=Player("moiz",6)
# p2=Player("moiz",6)
# print(p1.Player_count)

#Q.9]
# class Herbivore:

#     def display_herbivore(self):
#         print("haryali khate")

# class Carnivore:
#     def display_carnivore(self):
#          print("gosh khate")

# class Omnivore:
#     def display_omnivore(self):
#         print("eat both")

# class Bear(Herbivore,Carnivore,Omnivore):
#      def display_Omnivore():
#         print("eat both")

# b1=Bear()
# b1.display_carnivore()
# b1.display_omnivore()