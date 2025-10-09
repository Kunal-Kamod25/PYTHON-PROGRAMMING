n = int(input("Enter the number of elements: "))
A = []
print("Enter the elements:")
for i in range(n):
    A.append(int(input()))

i = n - 1
j = 0

while j < i:
    c = A[j]
    A[j] = A[i]
    A[i] = c
    j += 1
    i -= 1
print("Final array is:", A)
