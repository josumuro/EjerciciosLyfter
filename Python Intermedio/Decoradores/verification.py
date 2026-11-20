def verification(func):
    def wrapper(*args, **kwargs):  
        
        print(f"Parameters: {args}, {kwargs}")

        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError(f"The parameter '{arg}' is not a number.")
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise ValueError(f"The parameter '{key}' with value '{value}' is not a number.")
        return func(*args, **kwargs)
    return wrapper

@verification
def suma(a, b):
    return a + b
print(suma(3, 5))  
print(suma(3, "a"))