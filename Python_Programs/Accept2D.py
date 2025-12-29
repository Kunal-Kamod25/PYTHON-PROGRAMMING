n = int(input("Enter n: "))
arr = [[0 for _ in range(n)] for _ in range(n)]

print("Enter the elements of the array:")

# Read matrix elements
for row in range(n):
    for col in range(n):
        arr[row][col] = int(input())
