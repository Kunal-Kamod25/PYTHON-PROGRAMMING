n = int(input("Enter array size: "))

print("Enter array elements:")
a = []
for i in range(n):
    a.append(int(input()))

max_val = a[0]
min_val = a[0]

for i in range(1, n):
    if a[i] > max_val:
        max_val = a[i]
    if a[i] < min_val:
        min_val = a[i]

print("max =", max_val)
print("min =", min_val)
