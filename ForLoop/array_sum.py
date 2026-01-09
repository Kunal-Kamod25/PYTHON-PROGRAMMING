# Read number of rows and columns
rows = int(input("Enter the rows: "))
colms = int(input("Enter the columns: "))

# Read matrix elements
print("Enter the elements of matrix:")
matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Calculate and display sum of each row
for i in range(rows):
    row_sum = sum(matrix[i])
    print(f"Sum of row {i + 1} = {row_sum}")
