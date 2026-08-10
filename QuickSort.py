# Quick Sort

import time


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# User Input
arr = list(map(int, input("Enter elements separated by space: ").split()))

print("Original array:", arr)

start = time.perf_counter()

quick_sort(arr, 0, len(arr) - 1)

end = time.perf_counter()

print("Sorted array:", arr)
print("Execution time:", end - start, "seconds")

print("Best Case: O(n log n)")
print("Average Case: O(n log n)")
print("Worst Case: O(n^2)")
print("Space Complexity: O(log n) average")