#Q.1] create online store and track totale product being created
class Store:
    count=0

    def __init__ (self,product,price):
        self.product=product
        self.price=price
        Store.count+=1
       # self.count+=1 , creates new variable but we need class's variable count

    def display_info(self):
        print(f"product : {self.product} , price :  {self.price}")
    @classmethod
    def product_count(cls):
      print("totale products are : ",cls.count)
    @staticmethod
    def calc_discount(price,discount):
      print(f"discounted price = {price-(price*discount/100)}")


p1 = Store("laptop",15000)
p2 = Store("ear phones",9000)
p3 = Store("charger",5000)
p3 = Store("pen",5)
p1.display_info()
p2.display_info()
print(Store.count)
p2.calc_discount(p2.price,50)
