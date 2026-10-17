from datetime import date, datetime

def decorator_multi(func):
    def wrapper(a, b):
        return func(a, b)
    return wrapper

@decorator_multi
def function_name(a, b):
    return a * b
    pass

print(function_name)

def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs} at {datetime.now()}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper


def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError(f"El argumento '{arg}' no es un número.")
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise ValueError(f"El argumento '{key}' con valor '{value}' no es un número.")
        return func(*args, **kwargs)
    return wrapper



@log_call
@validate_numbers
def multiply(a, b):
    return a * b

print(multiply(3, 5))
print(multiply(3, "a"))  # Esto lanzará una excepción ValueError debido a la validación de números.


