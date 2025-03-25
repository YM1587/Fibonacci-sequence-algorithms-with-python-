def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        fibonacci_recursive=fibonacci(n-1)
        fibonacci_recursive.append(fibonacci_recursive[-1] + fibonacci_recursive[-2])
        return fibonacci_recursive

print(fibonacci(15))
    