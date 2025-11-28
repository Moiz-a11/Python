class Employee:
    start_time= "7 pm"
    end_time= "5 pm"


class Teacher(Employee):
    def __init__(self,sub):
        self.sub=sub

t1=Teacher("math")
print(t1.start_time)
print(t1.end_time)