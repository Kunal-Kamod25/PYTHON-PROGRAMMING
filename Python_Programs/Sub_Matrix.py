n = int(input("Enter size of Matrix: "))

print("Enter first Matrix:")
m1 = []
for r in range(n):
    row = list(map(int, input().split()))
    m1.append(row)

print("Enter Second Matrix:")
m2 = []
for r in range(n):
    row = list(map(int, input().split()))
    m2.append(row)

print("First Matrix is:")
for r in range(n):
    for c in range(n):
        print(m1[r][c], end=" ")
    print()

print("Second Matrix is:")
for r in range(n):
    for c in range(n):
        print(m2[r][c], end=" ")
    print()

# subtraction matrix
sub = [[0] * n for _ in range(n)]
print("Subtraction Matrix is:")
for r in range(n):
    for c in range(n):
        sub[r][c] = m1[r][c] - m2[r][c]
        print(sub[r][c], end=" ")
    print()
