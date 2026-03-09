# Read number of rows and columns
rows = int(input("Enter the Rows: "))
colms = int(input("Enter the Columns: "))

# Read matrix elements
print("Enter the Elements of Matrix:")
matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Calculate and display sum of each column
for j in range(colms):
    col_sum = 0
    for i in range(rows):
        col_sum += matrix[i][j]
    print(f"Sum of column {j + 1} = {col_sum}")
