# Read number of rows and columns
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Create empty matrix
a = [[0 for _ in range(cols)] for _ in range(rows)]

print("Enter elements of matrix:")

# Read matrix elements
for i in range(rows):
    for j in range(cols):
        a[i][j] = int(input())

# Print the matrix
print("\nMatrix is:")
for i in range(rows):
    for j in range(cols):
        print(a[i][j], end="\t")
    print()
