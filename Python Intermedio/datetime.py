from datetime import datetime


class TimestampMixin:
    def __init__(self):
        self._created_at = datetime.now()

    def when_created(self):
        return f"Created on {self._created_at.strftime('%Y-%m-%d')} at {self._created_at.strftime('%H:%M:%S')}"

class DiscountMixin:
    def apply_discount(self, percent):
        return self.price * (1 - percent / 100)


class Order(TimestampMixin):
    def __init__(self, number, total):
        super().__init__()
        self.order_id = number
        self.total = total


class Product(TimestampMixin, DiscountMixin):   # ← dos bases aquí
    def __init__(self, name, price):
        super().__init__()
        self.name  = name
        self.price = price

product = Product("Laptop", 999.99)
order   = Order(12345, 1999.99)

print(product.when_created())           # de TimestampMixin
print(product.apply_discount(10))       # de DiscountMixin → 899.991
print(order.when_created())             # de TimestampMixin