n = 3
A = [[0] * n for _ in range(n)]

r = int(input("Enter row: "))
c = int(input("Enter column: "))

print("Enter matrix elements:")
for i in range(r):
    for j in range(c):
        A[i][j] = int(input())

# Print matrix
for i in range(r):
    for j in range(c):
        print(A[i][j], end=" ")
    print()

print()  # Blank line

# Print lower triangular (i > j)
for i in range(r):
    for j in range(c):
        if i > j:
            print(A[i][j], end="\t")
        else:
            print("0", end="\t")
    print()
