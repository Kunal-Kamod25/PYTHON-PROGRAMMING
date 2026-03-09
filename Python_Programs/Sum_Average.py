n = int(input("Enter array size: "))

print("Enter array elements:")
a = []
for i in range(n):
    a.append(int(input()))

total = 0.0
for i in range(n):
    total += a[i]

print("sum =", total)
print("average =", total / n)
