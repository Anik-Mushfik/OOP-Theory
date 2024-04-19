# def decorator(func):
#     def wrapper():
#         print("Something is happening before the target function is called.")
#         func()
#         print("Something is happening after the target function is called.")
#     return wrapper

# def target():
#     print("I am a target function!")

# target = decorator(target)
# target()



# def decorator(func):
#     def wrapper():
#         print("Something is happening before the target function is called.")
#         func()
#         print("Something is happening after the target function is called.")
#     return wrapper

# @decorator
# def target():
#     print("I am a target function!")

# target()



# def decorator_function(original_fuvtion):
#     def wrapper_function(*args, **kwargs):
#         print("Wrapper exicuted this before {}".format(original_fuvtion.__name__))
#         # return original_fuvtion()
#         original_fuvtion(*args, **kwargs)
#         # use (*args) and (*kwargs), so that no error happens even if you use arguments in decorated function.
#         # else this error happens=> TypeError: decorator_function.<locals>.wrapper_function() takes 0 positional arguments but 2 were given
#         print(f"Wrapper exicuted this after {original_fuvtion.__name__}")
        
#     return wrapper_function

# def display():
#     print("Display function ran!")

# decorated_display = decorator_function(display)
# decorated_display()

### => @decorator_function means: display = decorator_function(display) ; display()

# @decorator_function
# def dissplay():
#     print("This is tthe right way of using decorator")

# dissplay()


# @decorator_function
# def display_info(name, age):
#     print(f"display_info ran with arguments ({name}, {age})")

# display_info('Jhon', 35)



# ## Decorator class:=>

# class Decorator_class(object):
#     def __init__(self, original_fuvtion):
#         self.original_fuvtion = original_fuvtion

#     def __call__(self, *args, **kwargs):
#         print(f"call method exicuted this before {self.original_fuvtion.__name__}")
#         self.original_fuvtion(*args, **kwargs) 
#         # when you pass *args and **kwargs in the original function they use it to call the decorated function, so its important to pass those in the original function.


# @Decorator_class
# def dissplay():
#     print("This is tthe right way of using decorator")

# dissplay()


# @Decorator_class
# def display_info(name, age):
#     print(f"display_info ran with arguments ({name}, {age})")

# display_info('Jhon', 35)




def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f"{orig_func.__name__}.log", level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            f"Ran with args: {args} & kwargs: {kwargs}"
        )
        return orig_func(*args, **kwargs)

    return wrapper



@my_logger
def display_info(name, age):
    print(f"display_info ran with arguments ({name}, {age})")

display_info('Abid', 23)