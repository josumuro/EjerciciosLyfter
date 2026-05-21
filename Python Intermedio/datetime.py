from datetime import datetime

class TimestampMixin:
    def when_created(self):                          
        now = datetime.now()
        return f"Created on {now.strftime('%Y-%m-%d')} at {now.strftime('%H:%M:%S')}"

class Product(TimestampMixin):
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order(TimestampMixin):
    def __init__(self, number, total):
        self.order_id = number
        self.total = total

product = Product("Laptop", 999.99)
order   = Order(12345, 1999.99)

print(product.when_created())   # Created on 2025-05-21 at 14:32:10
print(order.when_created())     # Created on 2025-05-21 at 14:32:10
# Ninguna de las dos definió el método — lo tienen por el Mixin