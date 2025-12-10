# Fixed matrix size like A[3][3]
A = [[0] * 3 for _ in range(3)]

r = int(input("Enter row: "))
c = int(input("Enter column: "))

print("Enter matrix elements:")
for i in range(r):
    for j in range(c):
        A[i][j] = int(input())

print("Matrix is:")
for i in range(r):
    for j in range(c):
        print(A[i][j], end=" ")
    print()
