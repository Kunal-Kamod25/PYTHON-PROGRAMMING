# Read size of the matrix
n = int(input("Enter the size of matrix: "))

# Read first matrix
print("Enter the first matrix:")
matrix1 = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix1.append(row)

# Read second matrix
print("Enter the second matrix:")
matrix2 = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix2.append(row)

# Subtract matrices
result = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(matrix1[i][j] - matrix2[i][j])
    result.append(row)

# Display result
print("Subtraction of matrices:")
for row in result:
    print(*row)
