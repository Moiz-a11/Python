
class Laptop:
    storage_type ="ssd"

    def __init__(self,RAM,storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod # it is a decorator
    def get_storage(cls):
        print(cls.storage_type) # printing the class's storage_type 

    def get_info(self): # instance method
        print(f"{self.RAM},{self.storage}")


l1=Laptop("16gb","512") 
l1.get_info()