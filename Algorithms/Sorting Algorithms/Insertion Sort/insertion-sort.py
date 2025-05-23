# Insertion Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)


def insertion_sort(arr):
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Place key at after the element just smaller than it.
        arr[j + 1] = key


arr = [23, 8, 5, 12, 35, 82, 25, 20]
print("Unsorted array:", arr)
insertion_sort(arr)
print("Sorted array:", arr)