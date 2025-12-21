for i in range(1, 1000):
    temp = i
    total = 0

    while temp > 0:
        rem = temp % 10
        total += rem ** 3
        temp //= 10

    if total == i:
        print(i, "is an Armstrong number")
