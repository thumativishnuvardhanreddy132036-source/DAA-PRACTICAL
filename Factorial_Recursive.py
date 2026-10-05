import time

def fibonacci(n):
    if n == 0 or n == 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


# User input
n = int(input("Enter a number: "))

# Measure execution time
start = time.perf_counter()

result = fibonacci(n)

end = time.perf_counter()

# Output
print("Fibonacci Number:", result)
print("Time Complexity: O(2^n)")
print("Space Complexity: O(n)")
print("Execution Time:", end - start, "seconds")