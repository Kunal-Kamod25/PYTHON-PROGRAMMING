n = int(input("enter an n: "))

print("enter matrix:")
mat = []
for r in range(n):
    row = list(map(int, input().split()))
    mat.append(row)

mul = 1
for r in range(n):
    mul *= mat[r][1]   # second column

print("multiplication is =", mul)
