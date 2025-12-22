n = int(input("enter num: "))

print("enter array:")
a = []
for i in range(n):
    a.append(int(input()))

count_even = 0
count_odd = 0

for i in range(n):
    if a[i] % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print("count even no =", count_even)
print("count odd no =", count_odd)
