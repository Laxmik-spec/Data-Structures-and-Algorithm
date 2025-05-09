# The above code takes input from the user for the number of elements in the array and then takes input for each element.
# It then prints the elements in the array in two different ways: using a loop and directly printing the array.
# The first method is more efficient for large arrays, while the second method is more convenient for small arrays.
# The code can be improved by using list comprehension to create the array in a single line.

print("How many elements do you want to enter in the array? ")
n = int(input())
arr = []
for i in range(n):
    print("Enter the element: ")
    arr.append(int(input()))
print("The elements in the array are: ")
for i in range(n):
    print(arr[i], end=" ")
print("\nThe elements in the array are: ", arr)
