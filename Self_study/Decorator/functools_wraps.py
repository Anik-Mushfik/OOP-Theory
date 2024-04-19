""" 
The wraps function from the functools module in Python is a decorator itself. 
It is used to preserve metadata (such as the function name, docstring, and other attributes) 
of the original function when creating a decorator.

When you define a decorator function and apply it to another function, 
it's common practice to use wraps to ensure that the metadata of the original function is retained. 
This helps maintain the integrity of the original function's identity and documentation.

Here's a simple example to demonstrate the usage of wraps:
"""

from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before calling the original function")
        result = func(*args, **kwargs)
        print("After calling the original function")
        return result
    return wrapper

@decorator
def original_function():
    """This is the original function."""
    print("Inside the original function")

# Accessing metadata of the original function
print("Name of the function:", original_function.__name__)
print("Docstring of the function:", original_function.__doc__)

# Calling the decorated function
original_function()



"""
In this example, the @wraps(func) line inside the decorator function ensures that the metadata of the 
original_function (such as its name and docstring) is preserved when it's wrapped by the wrapper function. 
This allows you to access and use the metadata of the original function even after it's been decorated.
"""
