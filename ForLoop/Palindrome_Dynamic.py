n = int(input("enter the n elements: "))

print("enter array:")
arr = []
for i in range(n):
    arr.append(int(input()))

flag = True
i = 0
j = n - 1

while i < j:
    if arr[i] != arr[j]:
        flag = False
        break
    i += 1
    j -= 1

if flag:
    print("array is palindrome")
else:
    print("array is not palindrome")
