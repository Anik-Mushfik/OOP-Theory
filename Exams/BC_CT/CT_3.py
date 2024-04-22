### => Qustion no -1 :

def divide(x,y):
    try:
        result = x// y
    except ZeroDivisionError:
        print("Sorry! You need to do some math ")
    except ValueError:
        print("That doesnt make any sense")
    except TypeError:
        print("Now that's Confusing")
    except Exception:
        print("That is generalization")
    else:
        print(f"Yeah your answer is : {result}")
    finally:
        print("Go make some sense and rewrite")

divide('3',2)
divide(3,'a')
divide(3,0)
divide(10,2)


### => Qustion no -2 :



from functools import wraps

def func_name_printer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # print(f"Function that started runnig is {func.__name__}")
        print("Function that started runnig is ", func.__name__)
        return func(*args, **kwargs)
    return wrapper


@func_name_printer
def add(*args):
    tot_sum = 0
    for arg in args:
        tot_sum += arg
    print("Result = " + str(tot_sum))


@func_name_printer
def sub(*args):
    tot_sub = args[0] - args[1]
    print("Result :" + str(tot_sub))


@func_name_printer
def mul(*args):
    tot_mul = 1
    for i in args:
        tot_mul *= i
    print("Result :" + str(tot_mul))



add(1,2)
mul(1,2,3)
sub(400, 150)