# Merge Sort

import time


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# User Input
arr = list(map(int, input("Enter elements separated by space: ").split()))

print("Original array:", arr)

start = time.perf_counter()

merge_sort(arr)

end = time.perf_counter()

print("Sorted array:", arr)
print("Execution time:", end - start, "seconds")

print("Best Case: O(n log n)")
print("Average Case: O(n log n)")
print("Worst Case: O(n log n)")
print("Space Complexity: O(n)")