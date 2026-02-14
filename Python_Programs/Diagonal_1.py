# Read size of square matrix
n = int(input("Enter the size of Square Matrix: "))

# Create empty matrix
matrix = [[0 for _ in range(n)] for _ in range(n)]

print("Enter the elements of matrix:")

# Read matrix elements
for i in range(n):
    for j in range(n):
        matrix[i][j] = int(input())

# Print diagonal elements
print("Diagonal Elements:")
for i in range(n):
    print(matrix[i][i], end=" ")
print()
