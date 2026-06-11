import time
import functools

def timer(func):
    @functools.wraps(func)


    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} tardó {(end - start) * 1000:.2f} ms")
        return result
    return wrapper


@timer
def procesar(lista):
    return [x * 2 for x in lista]

resultado = procesar(list(range(100_000)))
print(resultado[:10])