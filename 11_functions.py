# def my_function():
#     pass

def my_decorator(func):
    def wrapper(*args, **kwargs):
        if not isinstance(args[0], int):
            raise ValueError("First input argument is not an integer")
        if not isinstance(args[1], int):
            raise ValueError("Second input argument is not an integer")
        
        if len(kwargs) > 0:
            key_list = list(kwargs.keys())
            if not isinstance(kwargs[key_list[0]], int):
                raise ValueError ("First option input argument is not an integer")
            if not isinstance(kwargs[key_list[1]], int):
                raise ValueError ("Second option input argument is not an integer")
        else:
            kwargs.setdefault("c", 0)
            kwargs.setdefault("d", 0)
        
        return func(*args, **kwargs)
    return wrapper
    
@my_decorator
def addition(a, b, c, d):
    # operation
    sum = a + b + c + d
    return sum

sum = addition(2, 3, c=4, d=5)
print(sum)
sum = addition(2, 3, c="c", d=5)
print(sum)


