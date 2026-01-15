n = int(input("Enter size of Matrix: "))

print("Enter matrix:")
m = []
for r in range(n):
    row = list(map(int, input().split()))
    m.append(row)

# print main diagonal
for i in range(n):
    print(m[i][i], end=" ")

# find max on diagonal
max_val = m[0][0]
for i in range(n):
    if m[i][i] > max_val:
        max_val = m[i][i]

print("\nmax =", max_val)
