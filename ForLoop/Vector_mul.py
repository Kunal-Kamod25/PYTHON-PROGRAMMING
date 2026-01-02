n = int(input("Enter the size of Matrix: "))

# Initialize matrix, vector, and result
matrix = []
vector = []
ans = [0] * n

print("Enter the elements of matrix:")
for r in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

print("Enter the elements of vector:")
vector = list(map(int, input().split()))

# Matrix-vector multiplication
for r in range(n):
    for c in range(n):
        ans[r] += matrix[r][c] * vector[c]

print("Resultant vector:")
for val in ans:
    print(val)
