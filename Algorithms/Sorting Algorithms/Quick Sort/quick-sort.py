# Quick Sort
# Time Complexity: O(n log n) on average, O(n^2) in the worst case
# Space Complexity: O(log n) due to recursive stack space

def Partition(arr, low, high):
    pivot = arr[high]  # Choosing the last element as pivot
    i = low - 1  # Pointer for the smaller element

    for j in range(low, high):
        if arr[j] < pivot:  # If current element is smaller than or equal to pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap the pivot element with the element at i + 1
    return i + 1  # Return the partitioning index


def quick_sort(arr, low, high):
    if low < high:
        pi = Partition(arr, low, high)  # Partitioning index

        quick_sort(arr, low, pi - 1)  # Recursively sort elements before partition
        quick_sort(arr, pi + 1, high)  # Recursively sort elements after partition


arr = [23, 8, 5, 12, 35, 82, 25, 20]
print("Unsorted array:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)

