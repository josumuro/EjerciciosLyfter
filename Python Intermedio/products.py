class Product:
    def __init__(self,name:str,price:float, stock:int):
        self.name=name
        self.price=price
        self.stock=stock
    def __repr__(self):
        return f"Product(Name={self.name}, Price={self.price}, Stock={self.stock})"
    
class Inventory:
    def __init__(self):
        self.products=[]
    def add_product(self,product:Product):
        self.products.append(product)
    def remove_product(self,product:Product):
        self.products.remove(product)
    def get_total_value(self):
        return sum(product.price*product.stock for product in self.products)
    def total_stock(self):
        return sum(product.stock for product in self.products)
    
inventory=Inventory()
product1=Product("Laptop",1000.0,5)
product2=Product("Smartphone",500.0,10)
inventory.add_product(product1)
inventory.add_product(product2)
print(inventory.get_total_value())
print(inventory.total_stock())
