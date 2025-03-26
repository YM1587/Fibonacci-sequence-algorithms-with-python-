def fibonacci_generator(n):
    a, b = 0, 1  # Initialize first two Fibonacci numbers
    for _ in range(n):  # Loop n times
        yield a  # Yield the current Fibonacci number
        a, b = b, a + b  # Update 'a' and 'b' to the next numbers

print(list(fibonacci_generator(5)))
