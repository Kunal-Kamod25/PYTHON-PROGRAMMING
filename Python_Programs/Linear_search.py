n = int(input("enter a num: "))

print("enter array elements:")
a = []
for i in range(n):
    a.append(int(input()))

key = int(input("enter the key: "))

found = False
for i in range(n):
    if a[i] == key:
        print("key is found =", i)
        found = True
        break

if not found:
    print("not found key")
