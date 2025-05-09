# sort elements of an array in ascending order
# This program takes input from the user for the number of elements in the array and then takes input for each element.
# It then sorts the array in ascending order and prints the sorted array.

n = int(input("How many elements do you want to enter in the array? "))
arr = []
print("Enter the element: ")
for i in range(n):
    arr.append(int(input()))
print("\nArray elements: ", arr)
# arr.sort()
for i in range(n):
    for j in range(i+1, n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print("\nSorted Array: ", arr)