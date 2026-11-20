from os import name

from aiohttp_retry import abstractmethod

class Product:
 def __init__(self,name,price):
  self.name = name
  self.__price = price


def set_price(self,p):
  if p > 0:
   self.__price = p
  else:print("Precio debe ser mayor a 0")

@abstractmethod
def calculate_total(self):
 raise NotImplementedError("Subclase debe implementar este método")


class DigitalProduct(Product):
  def calculate_total(self):
   return self._Product__price


class PhysicalProduct(Product):
 _shipping_cost = 5.0    
 def calculate_total(self):
  return self._Product__price + self._shipping_cost
 
def print_cart(products):
 for p in products:
  print(f"{p.name}: Total = {p.calculate_total()}")

# Demo
digital = DigitalProduct("Ebook", 10.0)
physical = PhysicalProduct("Libro Físico", 20.0)    
print_cart([digital, physical])

from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def set_price(self, p):
        if p > 0:
            self.__price = p
        else:
            print("Precio debe ser mayor a 0")

    def get_price(self):
        return self.__price

    @abstractmethod
    def calculate_total(self): pass


class DigitalProduct(Product):
    def calculate_total(self):
        return self.get_price()


class PhysicalProduct(Product):
    def __init__(self, name, price, shipping_cost=5.0):
        super().__init__(name, price)
        self._shipping_cost = shipping_cost

    def calculate_total(self):
        return self.get_price() + self._shipping_cost


def print_cart(products):
    for p in products:
        print(f"{p.name}: Total = ${p.calculate_total():.2f}")


# Demo
digital = DigitalProduct("Ebook", 10.0)
physical = PhysicalProduct("Libro Físico", 20.0)
print_cart([digital, physical])

# Verificar encapsulamiento
digital.set_price(-5)       # Precio debe ser mayor a 0
digital.set_price(15)
print_cart([digital])       # $15.00

# Verificar que Product no se puede instanciar
try:
    Product("test", 10)
except TypeError as e:
    print(f"Error esperado: {e}")