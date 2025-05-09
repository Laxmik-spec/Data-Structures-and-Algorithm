# This program creates a 2D array and initializes it with the product of its indices.

rnum = int(input("Enter the number of rows: "))
cnum = int(input("Enter the number of columns: "))
arr = [[0 for col in range(cnum)] for row in range(rnum)]
for i in range(rnum):
    for j in range(cnum):
        arr[i][j] = i*j
print("2D array: ",arr)