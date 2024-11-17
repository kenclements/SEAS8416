def fibonacci(k):
    # Base Case
    if k == 0:
        return 0
    elif k == 1 or k == 2:
        return 1
    else:
        # Recursive Case
        return fibonacci(k-1) + fibonacci(k-2)

print(fibonacci(9))