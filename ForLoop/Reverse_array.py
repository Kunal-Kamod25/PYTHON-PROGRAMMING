# Read number of elements
n = int(input("Enter n elements: "))

# Read array elements
arr = []
print("Enter array:")
for i in range(n):
    arr.append(int(input()))

# Reverse the array using two-pointer method
i = n - 1
j = 0

while j < i:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    j += 1
    i -= 1

# Print reversed array
print("Reversed array:")
for x in arr:
    print(x, end=" ")
print()
