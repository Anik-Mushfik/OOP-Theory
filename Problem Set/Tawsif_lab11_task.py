# Qustion - 1:
import functools


def log_args_and_return(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function name : {func._name_}")
        if (kwargs == {}):
            print(f"Arguments : {args}")
        else:
            print(f"Arguments : {args, kwargs}")
        return func(*args, **kwargs)
    return wrapper


@log_args_and_return
def add(a, b):
    return a + b
result = add(3, 5)

print(f"Return Value: {result}")






# Qustion - 2:
def my_range(*args):
    start, stop, step= 0,0,1

    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start, stop = args
    elif len(args) == 3:
        start, stop, step = args


    if start < stop:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start += step


for i in my_range(5, 1, -1):
    print(i)

for i in my_range(5):
    print(i)

for i in my_range(1, 10, 2):
    print(i)