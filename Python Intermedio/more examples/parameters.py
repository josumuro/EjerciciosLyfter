def decorator_name(func):
    def wrapper(parameters):
        
        func(parameters) 
				

    return wrapper

@decorator_name
def function_name(parameters):
   
    pass

print(function_name)


def decorator_name(func):
    def wrapper(*args, **kwargs):
        print(f"Parámetros: args={args}, kwargs={kwargs}")
        
        result = func(*args, **kwargs)
        
        print(f"Retorno: {result}")
        return result

    return wrapper

@decorator_name
def function_name(a, b):
    return a + b

function_name(3, 5)
