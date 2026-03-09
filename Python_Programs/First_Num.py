n, m = map(int, input("Enter a n and m: ").split())

i = n + 1
while True:
    if i % m == 0:
        print(i)
        break
    i += 1
