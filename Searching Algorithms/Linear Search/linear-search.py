# Linear Search
# This code implements a linear search algorithm to find a target value in an array.   
# It iterates through each element in the array and checks if it matches the target value.


def linear_search(arr, target):
    """
    Perform a linear search on the array to find the target value.

    :param arr: List of elements to search
    :param target: Value to search for
    :return: Index of the target value if found, otherwise -1
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1
# Example usage
if __name__ == "__main__":
    arr = [5, 3, 8, 6, 2]
    target = 32
    result = linear_search(arr, target)
    if result != -1:
        print(f"Element {target} found at index {result}.")
    else:
        print(f"Element {target} not found in the array.")