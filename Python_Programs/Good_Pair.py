n = int(input("Enter array: "))

print("enter array elements:")
A = [int(input()) for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if A[i] == A[j]:
            print(f"({i},{j})", end="")
            cnt += 1

print(f"\nthere are {cnt} good pair:")
