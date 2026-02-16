n = int(input("Enter Number: "))
num = 1
i = 1

while i <= n:
    for j in range(1, n + 1):
        if (i + j) % 2 == 0:
            print(num, end=" ")
            num += 1
        else:
            print("- ", end="")
    print()
    i += 1
