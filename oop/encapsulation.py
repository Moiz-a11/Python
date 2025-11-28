
class BankAcount:

    def __init__(self,balance,id):
     self.__balance = balance # make private using two underscores, and protected use single underscore 
     self.id=id

# getter
    def get_balance(self):
      return self.__balance
    
# setter
    def set_balance(self,newBalance):
      self.__balance= newBalance
  
a1 = BankAcount(9000,12)
print(a1.get_balance())
a1.set_balance(2000)
print(a1.get_balance()) 