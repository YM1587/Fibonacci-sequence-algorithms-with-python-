def fibonacci(n):
    fibonacci_sequence = [0,1] #initialize with the first two numbers
    for i in range (2,n): #start from index 2 and go up to n
        fibonacci_sequence.append(fibonacci_sequence[-1]+fibonacci_sequence[-2]) #add last two numbers
    return fibonacci_sequence[:n] #return only upto n elements
#(:n)is a list slicing function that is used to take everything from index 0 - index n (but not including) 

print(fibonacci(20))

# Why Use This Approach?
# ✅ Easy to understand
# ✅ Fast and efficient for small sequences
# ❌ Uses extra memory (stores all numbers in a list)