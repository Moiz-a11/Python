
class Teacher:
    def __init__(self,salary):
        self.salary=salary

class Student:
    def __init__(self,gpa):
        self.gpa=gpa     


class TA(Teacher,Student):
    def __init__(self,salary,gpa,name):
        super().__init__(salary)
        Student.__init__(self, gpa)

        self.name=name


t1=TA(4000,9.8,"moiz")
print(t1.name,t1.gpa,t1.salary)