## You Tube ===>>>

def decorator_function(original_fuvtion):
    def wrapper_function(*args, **kwargs):
        print("Wrapper exicuted this before {}".format(original_fuvtion.__name__))
        # return original_fuvtion()
        original_fuvtion(*args, **kwargs)
        # use (*args) and (*kwargs), so that no error happens even if you use arguments in decorated function.
        # else this error happens=> TypeError: decorator_function.<locals>.wrapper_function() takes 0 positional arguments but 2 were given
        print(f"Wrapper exicuted this after {original_fuvtion.__name__}")
        
    return wrapper_function

def display():
    print("Display function ran!")

decorated_display = decorator_function(display)
decorated_display()

## => @decorator_function means: display = decorator_function(display) ; display()

@decorator_function
def dissplay():
    print("This is tthe right way of using decorator")

dissplay()


@decorator_function
def display_info(name, age):
    print(f"display_info ran with arguments ({name}, {age})")

display_info('Jhon', 35)



## Decorator class:=>

class Decorator_class(object):
    def __init__(self, original_fuvtion):
        self.original_fuvtion = original_fuvtion

    def __call__(self, *args, **kwargs):
        print(f"call method exicuted this before {self.original_fuvtion.__name__}")
        self.original_fuvtion(*args, **kwargs) 
        # when you pass *args and **kwargs in the original function they use it to call the decorated function, so its important to pass those in the original function.


@Decorator_class
def dissplay():
    print("This is tthe right way of using decorator")

dissplay()


@Decorator_class
def display_info(name, age):
    print(f"display_info ran with arguments ({name}, {age})")

display_info('Jhon', 35)


from functools import wraps

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f"{orig_func.__name__}.log", level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            f"Ran with args: {args} & kwargs: {kwargs}"
        )
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{orig_func.__name__} ran in: {t2} sec")
        return result
    
    return wrapper

import time

@my_logger
@my_timer
def display_info(name, age):
    time.sleep(2)
    print(f"display_info ran with arguments ({name}, {age})")

display_info('Tom', 32)

## This double decorators stacked on each other means=> display_info = my_logger(my_timer(display_info))



## Swakhar sir ===>>>

def decorator(func):
    def wrapper():
        print("Something is happening before the target function is called.")
        func()
        print("Something is happening after the target function is called.")
    return wrapper

def target():
    print("I am a target function!")

target = decorator(target)
target()


## =>Syntactic Sugar

def decorator(func):
    def wrapper():
        print("Something is happening before the target function is called.")
        func()
        print("Something is happening after the target function is called.")
    return wrapper

@decorator
def target():
    print("I am a target function!")

target()



from datetime import datetime

def not_during_night(func):
    def wrapper():
        if (7 <= datetime.now().hour <=22):
            print(f"It's {datetime.now().hour}:{datetime.now().minute}; You can play music now.")
            # return func()
            func()
        else:
            print(f"Hush! It's {datetime.now().hour}'o clock at night!\nThe neighbours are sleeping...")

    return wrapper

@not_during_night
def target():
    print("Playing Music...")

# target = not_during_night(target)
target()



## => Functions With Arguments

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper_do_twice

@do_twice
def target():
    print("Weee!")
target()

@do_twice
def greet(name):
    print(f"HI {name}")
greet("Anik")



### => Returning Values From Decorated Functions

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice

@do_twice
def return_greet(name):
    print(f"Creating Greetings!")
    return f"Hi {name}"

print(return_greet("Anik"))
"""
Python first reads all the lines and comes to line 198 finds a call then goes to the 194 function and
finds the decorator and goes to the decorator first and then goes to the wrapper function.
there it at first just calls the return greet fuction, so the print statement prints 
but the return statement isn't exicuted as it isn't set to anything.
while, the call of 189 line is a return so the "func" function (which is the 'return_greet' function) 
is returned to the wrapper function, which is returned to the decorator(which is the updated version of return_greet function)
so when the reurn_greet fuction is printed, the returned fsting of the fuction is printed in the console
"""



### => Identity of the target
from functools import wraps

def do_twice(func):
    @wraps(func) #wraps takes the same parameter of the decorator function
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return  func(*args, **kwargs)
    return wrapper

@do_twice
def return_greet(name):
    print(f"Creating Greetings!")
    return f"Hi {name}"

print(return_greet("Anik"))


### => Usecase 1: Timing of Functions
from functools import wraps
import time

def timer(func):
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__} in {run_time:.4f} secs.")
        return value
    
    return wrapper_timer


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([number**2 for number in range(100000)])
    # time.sleep(num_times)

waste_some_time(1)
waste_some_time(9)



### => Usecase 2: Debugging
import functools

def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__}() returned {repr(value)}")
        return value
    
    return wrapper_debug


@debug
def fibonacci(n):
    if n==1 or n==0:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(5))


### => Register of functions


PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we're the awesomest!"

print(PLUGINS)




PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func("Anik")

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we're the awesomest!"

print(say_hello)
print(be_awesome)
print(PLUGINS)
