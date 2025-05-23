#  search element in array
# This program takes input from the user for the number of elements in the array and then takes input for each element.
# It then searches for the specified element in the array and prints the index of the element if found, or a message if not found.

n = int(input("How many elements do you want to enter in the array? "))
arr = []
print("Enter the element: ")

for i in range(n):
    arr.append(int(input()))

print("\nArray Elements: ", arr)
val = int(input("Enter the element you want to search: "))
found = False
for i in range(n):
    if arr[i] == val:
        found = True
        print("Element found at index: ", i)
        break
if not found:
    print("Element not found in the array")