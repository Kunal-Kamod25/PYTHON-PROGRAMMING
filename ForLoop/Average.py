n = int(input("Enter a number: "))
A = []

print("Enter array elements:")
for i in range(n):
    A.append(int(input()))

# Calculate sum
total = sum(A)

print("sum =", total)

# Calculate average
avg = total / n
print("average of the array elements =", avg)
