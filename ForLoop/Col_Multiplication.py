n = int(input("Enter an number: "))

print("Enter matrix:")
mat = []
for r in range(n):
    row = list(map(int, input().split()))
    mat.append(row)

mul = 1
for r in range(n):
    mul *= mat[r][1]   # second column (index 1)

print("multiplication is =", mul)
