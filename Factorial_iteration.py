import time

def sum_numbers(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total


# User input
n = int(input("Enter a number: "))

# Measure execution time
start = time.perf_counter()

result = sum_numbers(n)

end = time.perf_counter()

# Output
print("Sum of Numbers:", result)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")
print("Execution Time:", end - start, "seconds")