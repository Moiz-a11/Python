

# 1] function overriding


class Employee:
   def display(self):
      print("function of Employee")
      

class Teacher(Employee):
   def display(self):
      print("function of Teacher")
      


t1=Teacher()
t1.display()

# 2] Duck typing
#two different class having same function
class Wwe:
   def display(self):
      print("function of wwe")
      

class Wwf:
   def display(self):
      print("function of wwf")
      
