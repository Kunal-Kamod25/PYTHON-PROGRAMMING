# Initial value but will be overwritten by user input
n = int(input("Size of Matrix: "))

# Create an n x n matrix
A = [[0] * n for _ in range(n)]

# Input matrix elements
for i in range(n):
    for j in range(n):
        A[i][j] = int(input())

# Print the matrix
for i in range(n):
    for j in range(n):
        print(A[i][j], end=" ")
    print()

# Print the main diagonal elements
for i in range(n):
    print(A[i][i], end="\t")
print()
