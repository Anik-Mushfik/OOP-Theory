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



def decorator_function(original_fuvtion):
    def wrapper_function():
        return original_fuvtion()
    return wrapper_function

def display():
    print("Display Message!")

decorated_display = decorator_function(display)
decorated_display()