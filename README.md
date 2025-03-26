# Fibonacci Sequence in Python

## Description
This project provides three different implementations of the Fibonacci sequence in Python:
1. **Iterative Approach** - Uses a loop to generate the sequence efficiently.
2. **Recursive Approach** - Uses recursion to generate the sequence but can be inefficient for large values of `n`.
3. **Generator Approach** - Uses Python generators (`yield`) to efficiently generate Fibonacci numbers without storing them in memory.

## Implementations

### 1. Iterative Approach
```python
def fibonacci(n):
    fib_sequence = [0, 1]  # Initialize with the first two numbers
    for i in range(2, n):  # Start from index 2 and go up to n
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])  # Add last two numbers
    return fib_sequence[:n]  # Return only up to n elements
```
**Usage:**
```python
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### 2. Recursive Approach
```python
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci_recursive(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq
```
**Usage:**
```python
print(fibonacci_recursive(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### 3. Generator Approach
```python
def fibonacci_generator(n):
    a, b = 0, 1  # First two numbers
    for _ in range(n):
        yield a  # Yield the current number
        a, b = b, a + b  # Update values
```
**Usage:**
```python
print(list(fibonacci_generator(10)))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## Choosing the Right Approach
| Approach | Time Complexity | Space Complexity | Best For |
|----------|----------------|-----------------|-----------|
| Iterative | O(n) | O(n) | Small sequences, simple cases |
| Recursive | O(2ⁿ) (slow) | O(n) (stack calls) | Conceptual understanding, small `n` |
| Generator | O(n) | O(1) | Large sequences, memory efficiency |

## Running the Code
To execute any of the implementations, save the code in a Python file (e.g., `fibonacci.py`) and run:
```sh
python fibonacci.py
```

## License
This project is open-source and available under the MIT License.

---
Enjoy coding Fibonacci in Python! 🚀

