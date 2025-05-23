# Binary search algorithm

def binary_search(arr, target):
    """
    Perform a binary search on a sorted array to find the target value.

    :param arr: List of sorted elements to search
    :param target: Value to search for
    :return: Index of the target value if found, otherwise -1
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if the target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore right half
        else:
            right = mid - 1

    # Target was not found in the array
    return -1

def binary_search_recursive(arr, target, left, right):
    """
    Perform a binary search on a sorted array to find the target value using recursion.

    :param arr: List of sorted elements to search
    :param target: Value to search for
    :param left: Left index of the subarray
    :param right: Right index of the subarray
    :return: Index of the target value if found, otherwise -1
    """
    if left > right:
        return -1

    mid = (left + right) // 2

    # Check if the target is present at mid
    if arr[mid] == target:
        return mid
    # If target is greater, ignore left half
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    # If target is smaller, ignore right half
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
    


# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5

print('Iterative Binary Search:')
result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")

print('\nRecursive Binary Search:')
res = binary_search_recursive(arr, target, 0, len(arr) - 1)
if res != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")