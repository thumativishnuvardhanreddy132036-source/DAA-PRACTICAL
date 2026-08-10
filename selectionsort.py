# Selection Sort

import time


def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


# User Input
arr = list(map(int, input("Enter elements separated by space: ").split()))

print("Original array:", arr)

start = time.perf_counter()

selection_sort(arr)

end = time.perf_counter()

print("Sorted array:", arr)
print("Execution time:", end - start, "seconds")

print("Best Case: O(n^2)")
print("Average Case: O(n^2)")
print("Worst Case: O(n^2)")
print("Space Complexity: O(1)")