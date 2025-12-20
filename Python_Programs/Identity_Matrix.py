r = int(input("Enter rows: "))
c = int(input("Enter columns: "))

print("Enter Matrix Elements:")
A = [[0] * c for _ in range(r)]

# Input matrix
for i in range(r):
    for j in range(c):
        A[i][j] = int(input())

# Convert to identity-style matrix
for i in range(r):
    for j in range(c):
        if i == j:
            A[i][j] = 1
        else:
            A[i][j] = 0

# Print the modified matrix
for i in range(r):
    for j in range(c):
        print(A[i][j], end=" ")
    print()
