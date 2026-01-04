n = int(input("Enter an Num: "))

print("enter array elements:")
a1 = []
for i in range(n):
    a1.append(int(input()))

print("original array")
for x in a1:
    print(x, end=" ")

# copy array
a2 = []
for i in range(n):
    a2.append(a1[i])

print("\ncopied array:")
for x in a2:
    print(x, end=" ")
