def divide_numbers(a, b):
    try:
        result = a / b
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Error: Division by zero!")
# Test cases
divide_numbers(10, 2)
divide_numbers(5, 0)
divide_numbers("10", 2)