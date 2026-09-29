n = int(input("Enter Array Size: "))

print("Enter Array Elements:")
a = []
for i in range(n):
    a.append(int(input()))

total = 0.0
for i in range(n):
    total += a[i]

print("Sum =", total)
print("Average =", total / n)
