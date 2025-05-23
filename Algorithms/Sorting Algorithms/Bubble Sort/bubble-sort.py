# Bubble Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)


# Recursive Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [23, 8, 5, 12, 35, 82, 25, 20]
print("Unsorted array:", arr)
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)