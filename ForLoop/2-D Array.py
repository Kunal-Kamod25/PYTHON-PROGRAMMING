# Matrix size (like int n = 3)
n = 3
A = [[0] * n for _ in range(n)]

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

# Printing the first row
for j in range(c):
    print(A[0][j], end=" ")

