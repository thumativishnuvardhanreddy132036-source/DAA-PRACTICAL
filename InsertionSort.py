# Insertion Sort

import time


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


# User Input
arr = list(map(int, input("Enter elements separated by space: ").split()))

print("Original array:", arr)

start = time.perf_counter()

insertion_sort(arr)

end = time.perf_counter()

print("Sorted array:", arr)
print("Execution time:", end - start, "seconds")

print("Best Case: O(n)")
print("Average Case: O(n^2)")
print("Worst Case: O(n^2)")
print("Space Complexity: O(1)")