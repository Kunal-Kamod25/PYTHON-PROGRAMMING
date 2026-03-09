n = int(input("Enter the number of Elements: "))

print("Enter the elements:")
arr = []
for i in range(n):
    arr.append(int(input()))

# count positive, negative, zero
pos = neg = zero = 0
for x in arr:
    if x > 0:
        pos += 1
    elif x < 0:
        neg += 1
    else:
        zero += 1

print(f"positive={pos}\t negative={neg}\t zero={zero}")

# print pairs with positive sum
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] > 0:
            print(arr[i], arr[j])
