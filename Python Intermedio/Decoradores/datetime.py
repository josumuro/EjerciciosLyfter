
from datetime import date


class User:
    def __init__(self, date_of_birth: date):
        self.date_of_birth = date_of_birth

    @property
    def age(self) -> int:
        today = date.today()
        years = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            years -= 1 
        return years

    def __repr__(self):
        return f"User(date_of_birth={self.date_of_birth}, age={self.age})"


def require_adult(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, User) and arg.age < 18:
                raise ValueError(f"User (age {arg.age}) is not an adult.")
        for key, value in kwargs.items():
            if isinstance(value, User) and value.age < 18:
                raise ValueError(f"User '{key}' (age {value.age}) is not an adult.")
        return func(*args, **kwargs)
    return wrapper


@require_adult
def register(user: User):
    print(f"Registered: {user}")


adult = User(date(1995, 3, 20))
minor = User(date(2012, 8, 10))

register(adult)

try:
    register(minor)
except ValueError as e:
    print(e)