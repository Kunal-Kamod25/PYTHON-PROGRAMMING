n = int(input("Enter a Number: "))

for i in range(2, n):
    for j in range(1, 12):
        print(f"{i}*{j}={i * j}")
