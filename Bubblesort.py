# Bubble Sort

import time


def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break


# User Input
arr = list(map(int, input("Enter elements separated by space: ").split()))

print("Original array:", arr)

start = time.perf_counter()

bubble_sort(arr)

end = time.perf_counter()

print("Sorted array:", arr)
print("Execution time:", end - start, "seconds")

print("Best Case: O(n)")
print("Average Case: O(n^2)")
print("Worst Case: O(n^2)")
print("Space Complexity: O(1)")