
# Selection Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element of the unsorted array
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

arr = [23, 8, 5, 12, 35, 82, 25, 20]
print("Unsorted array:", arr)
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)