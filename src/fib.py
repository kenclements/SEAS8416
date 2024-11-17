def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something before the function runs")
        result = func(*args, **kwargs)
        print("Something after the function runs")
        return result
    return wrapper

@my_decorator
def fibonacci(k):
    # Base Case
    if k == 0:
        return 0
    elif k == 1 or k == 2:
        return 1
    else:
        # Recursive Case
        return fibonacci(k-1) + fibonacci(k-2)

print(fibonacci(2))
