def calculate_sum(a, b):
    return a + b

def calculate_sub(a, b):
    return a - b

def calculate_multi(a, b):
    return a * b

def calculate_div(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        c = "error: Division by zero is not allowed"
    return c