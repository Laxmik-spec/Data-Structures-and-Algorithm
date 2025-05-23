# delete element from array
# This program takes input from the user for the number of elements in the array and then takes input for each element.
# It then deletes the element at the specified index and prints the updated array.

print("How many elements do you want to enter in the array? ")
n = int(input())
arr = []
print("Enter the element: ")
for i in range(n):
    arr.append(int(input()))
print("\nThe elements in the array are: ", arr)

val = int(input("Enter the element you want to delete: "))

if val in arr:
    arr.remove(val)
    print("\nThe elements in the array after deleting the element ", val, "are: ", arr)
else:
    print("Index out of range")