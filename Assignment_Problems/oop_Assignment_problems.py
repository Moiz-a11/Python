
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


class Vehicle:
    def __init__(self,brand,model):
        
        self.brand=brand
        self.model=model


class Car(Vehicle):
    def __init__(self,brand,model,seats):
        super().__init__(brand, model)  # call base class constructor
        self.seats=seats

    def Display_info(self):
        print("brand = ",self.brand)
        print("modeol = ",self.model)


class Bike(Vehicle):

    def __init__(self,brand,model,engine):
        super().__init__(brand, model)  # call base class constructor
        self.engine=engine



    def Display_info(self):
        print("brand = ",self.brand)
        print("modeol = ",self.model)


b1=Bike("yamaha","2022","high")
b1.Display_info()
