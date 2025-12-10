n = int(input("Enter size of matrix: "))

# Create matrix and vectors
m = [[0] * n for _ in range(n)]
v = [0] * n
ans = [0] * n

print("Enter matrix elements:")
for r in range(n):
    for c in range(n):
        m[r][c] = int(input())

print("Enter row vector:")
for r in range(n):
    v[r] = int(input())

# Initialize ans to 0
for r in range(n):
    ans[r] = 0

# Matrix-vector multiplication
for r in range(n):
    for c in range(n):
        ans[r] += m[r][c] * v[c]

print("Matrix-vector multiplication is:")
for r in range(n):
    print(ans[r], end=" ")
print()
